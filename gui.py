import os
import subprocess
import re
import requests
import threading
from zipfile import ZipFile
import customtkinter as ctk
from PIL import Image
from downloads import Downloads
from utils import Utils

class GUI:
    @staticmethod
    def gui():
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        root = ctk.CTk()
        root.configure(bg='#353746')
        root.attributes('-fullscreen', True)
        root.title("Installer")

        frame1 = ctk.CTkFrame(root)
        frame1.pack(side="top", fill='x', pady=20)

        frame2 = ctk.CTkFrame(root)
        frame2.pack(side="top", fill='x', pady=20)

        progress_label = ctk.CTkLabel(root, text="Download Progress:")
        progress_label.pack(pady=10)

        progress_bar = ctk.CTkProgressBar(root)
        progress_bar.pack(fill='x', padx=20, pady=10)
        progress_bar.set(0)

        # Pass the root and progress_bar to the Downloads class
        Downloads.root = root
        Downloads.progress_bar = progress_bar

        brave_image = Utils.image_resize((50, 50), "icons/brave_icon.png")
        vscode_image = Utils.image_resize((50, 50), "icons/vscode_icon.png")
        zip_image = Utils.image_resize((50, 50), "icons/7zip_icon.png")
        filterkeysetter_image = Utils.image_resize((50, 50), "icons/filterkeysetter_icon.png")
        rainmeter_image = Utils.image_resize((50, 50), "icons/rainmeter_icon.png")
        chrome_image = Utils.image_resize((50, 50), "icons/chrome_icon.png")
        notepadpp_image = Utils.image_resize((50, 50), "icons/notepadpp_icon.png")
        gimp_image = Utils.image_resize((50, 50), "icons/gimp_icon.png")
        git_image = Utils.image_resize((50, 50), "icons/git_icon.png")
        docker_image = Utils.image_resize((50, 50), "icons/docker_icon.png")
        slack_image = Utils.image_resize((50, 50), "icons/slack_icon.png")
        spotify_image = Utils.image_resize((50, 50), "icons/spotify_icon.png")
        python_image = Utils.image_resize((50, 50), "icons/python_icon.png")
        nodejs_image = Utils.image_resize((50, 50), "icons/nodejs_icon.png")
        obs_image = Utils.image_resize((50, 50), "icons/obs_icon.png")

        brave_button = ctk.CTkButton(
            frame1,  
            text="Brave",
            command=lambda: threading.Thread(target=Downloads.start_brave).start(),
            image=brave_image,
            compound="top",
            font=("Arial", 16, "bold"),
        )

        vscode_button = ctk.CTkButton(
            frame1,
            text="VSCode",
            command=lambda: threading.Thread(target=Downloads.start_vscode).start(),
            image=vscode_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        zip_button = ctk.CTkButton(
            frame1,
            text="7-Zip",
            command=lambda: threading.Thread(target=Downloads.start_7zip).start(),
            image=zip_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        filterkeysetter_button = ctk.CTkButton(
            frame1,
            text="Keysetter",
            command=lambda: threading.Thread(target=Downloads.start_filterkeysetter).start(),
            image=filterkeysetter_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        rainmeter_button = ctk.CTkButton(
            frame1,
            text="Rainmeter",
            command=lambda: threading.Thread(target=Downloads.start_rainmeter).start(),
            image=rainmeter_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        chrome_button = ctk.CTkButton(
            frame1,
            text="Chrome",
            command=lambda: threading.Thread(target=Downloads.start_chrome).start(),
            image=chrome_image,
            compound="top",
            font=("Arial", 16, "bold"),
        )

        notepadpp_button = ctk.CTkButton(
            frame1,
            text="Notepad++",
            command=lambda: threading.Thread(target=Downloads.start_notepadpp).start(),
            image=notepadpp_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        gimp_button = ctk.CTkButton(
            frame1,
            text="GIMP",
            command=lambda: threading.Thread(target=Downloads.start_gimp).start(),
            image=gimp_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        git_button = ctk.CTkButton(
            frame2,
            text="Git",
            command=lambda: threading.Thread(target=Downloads.start_git).start(),
            image=git_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        docker_button = ctk.CTkButton(
            frame2,
            text="Docker",
            command=lambda: threading.Thread(target=Downloads.start_docker).start(),
            image=docker_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        slack_button = ctk.CTkButton(
            frame2,
            text="Slack",
            command=lambda: threading.Thread(target=Downloads.start_slack).start(),
            image=slack_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        spotify_button = ctk.CTkButton(
            frame2,
            text="Spotify",
            command=lambda: threading.Thread(target=Downloads.start_spotify).start(),
            image=spotify_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        python_button = ctk.CTkButton(
            frame2,
            text="Python",
            command=lambda: threading.Thread(target=Downloads.start_python).start(),
            image=python_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        nodejs_button = ctk.CTkButton(
            frame2,
            text="Node.js",
            command=lambda: threading.Thread(target=Downloads.start_nodejs).start(),
            image=nodejs_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        obs_button = ctk.CTkButton(
            frame2,
            text="OBS",
            command=lambda: threading.Thread(target=Downloads.start_obs).start(),
            image=obs_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        brave_button.pack(padx=20, pady=20, side="left")
        vscode_button.pack(padx=20, pady=20, side="left")
        zip_button.pack(padx=20, pady=20, side="left")
        filterkeysetter_button.pack(padx=20, pady=20, side="left")
        rainmeter_button.pack(padx=20, pady=20, side="left")
        chrome_button.pack(padx=20, pady=20, side="left")
        notepadpp_button.pack(padx=20, pady=20, side="left")
        gimp_button.pack(padx=20, pady=20, side="left")

        git_button.pack(padx=20, pady=20, side="left")
        docker_button.pack(padx=20, pady=20, side="left")
        slack_button.pack(padx=20, pady=20, side="left")
        spotify_button.pack(padx=20, pady=20, side="left")
        python_button.pack(padx=20, pady=20, side="left")
        nodejs_button.pack(padx=20, pady=20, side="left")
        obs_button.pack(padx=20, pady=20, side="left")

        root.mainloop()

class Downloads:
    root = None
    progress_bar = None
    progress_lock = threading.Lock()

    @staticmethod
    def downloading(URL):
        try:
            response = requests.get(URL, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                return None

            filename = URL.split("/")[-1]
            filename = re.sub(r'[^\w\-_\. ]', '_', filename)

            if not os.path.exists('downloads'):
                os.makedirs('downloads')

            file_path = os.path.join('downloads', filename)
            total_length = int(total_length)

            downloaded = 0
            with open(file_path, "wb") as file:
                dl = 0
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    downloaded += len(data)
                    # Only update progress bar after a significant amount of data is downloaded
                    if downloaded > total_length / 100:  # update after 1% of total size
                        Downloads.update_progress(dl / total_length)
                        downloaded = 0

            Downloads.update_progress(1)  # ensure progress bar is filled at the end
            return file_path
        except Exception as e:
            print(f"Error downloading file: {e}")
            return None

    @staticmethod
    def update_progress(progress):
        with Downloads.progress_lock:
            if Downloads.root and Downloads.progress_bar:
                Downloads.root.after(0, Downloads.progress_bar.set, progress)

    @staticmethod
    def create_vbs_script(file_path):
        vbs_content = f'''
Set UAC = CreateObject("Shell.Application")
UAC.ShellExecute "cmd.exe", "/c {file_path}", "", "runas", 1
'''
        vbs_path = os.path.join(os.path.dirname(file_path), "elevate.vbs")
        with open(vbs_path, 'w') as vbs_file:
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