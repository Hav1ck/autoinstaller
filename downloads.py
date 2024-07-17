import os
import subprocess
import re
import requests
from zipfile import ZipFile

class Downloads:
    progress_bar = None

    @staticmethod
    def downloading(URL):
        try:
            response = requests.get(URL, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content
                return None

            filename = URL.split("/")[-1]
            filename = re.sub(r'[^\w\-_\. ]', '_', filename)

            if not os.path.exists('downloads'):
                os.makedirs('downloads')

            file_path = os.path.join('downloads', filename)
            total_length = int(total_length)

            with open(file_path, "wb") as file:
                dl = 0
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    if Downloads.progress_bar:
                        Downloads.progress_bar.set(dl / total_length)
            return file_path
        except Exception as e:
            print(f"Error downloading {URL}: {e}")
            return None

    @staticmethod
    def create_vbs_script(file_path):
        vbs_content = f"""
        Set UAC = CreateObject("Shell.Application")
        UAC.ShellExecute "{file_path}", "", "", "runas", 1
        """
        vbs_path = os.path.join(os.path.dirname(file_path), "elevate.vbs")
        with open(vbs_path, "w") as vbs_file:
            vbs_file.write(vbs_content)
        return vbs_path

    @staticmethod
    def open_file(file_path, admin=False):
        try:
            if admin:
                vbs_path = Downloads.create_vbs_script(file_path)
                subprocess.run(["wscript", vbs_path], check=True)
            else:
                subprocess.run([file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def open_msi(file_path, admin=False):
        try:
            if admin:
                vbs_path = Downloads.create_vbs_script(file_path)
                subprocess.run(["wscript", vbs_path], check=True)
            else:
                subprocess.run(["msiexec", "/i", file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening MSI file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def start_brave():
        print("Downloading Brave...")
        file_path = Downloads.downloading("https://github.com/brave/brave-browser/releases/download/v0.59.35/BraveBrowserSetup32.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_vscode():
        print("Downloading VSCode...")
        file_path = Downloads.downloading("https://vscode.download.prss.microsoft.com/dbazure/download/stable/f1e16e1e6214d7c44d078b1f0607b2388f29d729/VSCodeUserSetup-x64-1.91.1.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_7zip():
        print("Downloading 7-Zip...")
        file_path = Downloads.downloading("https://www.7-zip.org/a/7z2407-x64.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_filterkeysetter():
        print("Downloading FilterKeySetter...")
        zip_path = Downloads.downloading("https://wintools.b-cdn.net/FilterKeysSetter_1.0.zip")

        if zip_path:
            try:
                with ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall("downloads/filterkeysetter")

                exe_path = os.path.join("downloads", "filterkeysetter", "FilterKeysSetter.exe")
                Downloads.open_file(exe_path)
            except Exception as e:
                print(f"Error extracting or opening FilterKeySetter: {e}")

    @staticmethod
    def start_rainmeter():
        print("Downloading Rainmeter...")
        file_path = Downloads.downloading("https://github.com/rainmeter/rainmeter/releases/download/v4.5.18.3727/Rainmeter-4.5.18.exe")
        if file_path:
            Downloads.open_file(file_path, admin=True)

    @staticmethod
    def start_chrome():
        print("Downloading Google Chrome...")
        file_path = Downloads.downloading("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BD5F8B792-08D2-82D2-1316-2F4322602E09%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_notepadpp():
        print("Downloading Notepad++...")
        file_path = Downloads.downloading("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.8/npp.8.4.8.Installer.x64.exe")
        if file_path:
            Downloads.open_file(file_path, admin=True)

    @staticmethod
    def start_gimp():
        print("Downloading GIMP...")
        file_path = Downloads.downloading("https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.38-setup.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_git():
        print("Downloading Git...")
        file_path = Downloads.downloading("https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_docker():
        print("Downloading Docker Desktop...")
        file_path = Downloads.downloading("https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe")
        if file_path:
            Downloads.open_file(file_path, admin=True)

    @staticmethod
    def start_slack():
        print("Downloading Slack...")
        file_path = Downloads.downloading("https://downloads.slack-edge.com/desktop-releases/windows/x64/4.39.90/SlackSetup.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_spotify():
        print("Downloading Spotify...")
        file_path = Downloads.downloading("https://download.scdn.co/SpotifySetup.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_python():
        print("Downloading Python...")
        file_path = Downloads.downloading("https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe")
        if file_path:
            Downloads.open_file(file_path)

    @staticmethod
    def start_nodejs():
        print("Downloading Node.js...")
        file_path = Downloads.downloading("https://nodejs.org/dist/v18.17.1/node-v18.17.1-x64.msi")
        if file_path:
            Downloads.open_msi(file_path, admin=True)

    @staticmethod
    def start_obs():
        print("Downloading OBS Studio...")
        file_path = Downloads.downloading("https://cdn-fastly.obsproject.com/downloads/OBS-Studio-29.1.3-Full-Installer-x64.exe")
        if file_path:
            Downloads.open_file(file_path, admin=True)