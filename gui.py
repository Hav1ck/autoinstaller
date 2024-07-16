import os
import subprocess
import re
import requests
from zipfile import ZipFile
from PIL import Image
import customtkinter as ctk

class downloads:
    @staticmethod
    def downloading(URL):
        response = requests.get(URL)
        filename = URL.split("/")[-1]
        filename = re.sub(r'[^\w\-_\. ]', '_', filename)
        
        # Create the downloads directory if it doesn't exist
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        
        file_path = os.path.join('downloads', filename)
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_path
    
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
                vbs_path = downloads.create_vbs_script(file_path)
                subprocess.run(["wscript", vbs_path], check=True)
            else:
                subprocess.run([file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def start_brave():
        print("Downloading Brave...")
        file_path = downloads.downloading("https://github.com/brave/brave-browser/releases/download/v0.59.35/BraveBrowserSetup32.exe")
        downloads.open_file(file_path)

    @staticmethod
    def start_vscode():
        print("Downloading VSCode...")
        file_path = downloads.downloading("https://vscode.download.prss.microsoft.com/dbazure/download/stable/f1e16e1e6214d7c44d078b1f0607b2388f29d729/VSCodeUserSetup-x64-1.91.1.exe")
        downloads.open_file(file_path)

    @staticmethod
    def start_7zip():
        print("Downloading 7-Zip...")
        file_path = downloads.downloading("https://www.7-zip.org/a/7z2407-x64.exe")
        downloads.open_file(file_path, admin=True)

    @staticmethod
    def start_filterkeysetter():
        print("Downloading FilterKeySetter...")
        zip_path = downloads.downloading("https://wintools.b-cdn.net/FilterKeysSetter_1.0.zip")
        
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("downloads/filterkeysetter")

        exe_path = os.path.join("downloads", "filterkeysetter", "FilterKeysSetter.exe")
        downloads.open_file(exe_path)

    @staticmethod
    def start_rainmeter():
        print("Downloading Rainmeter...")
        file_path = downloads.downloading("https://github.com/rainmeter/rainmeter/releases/download/v4.5.18.3727/Rainmeter-4.5.18.exe")
        downloads.open_file(file_path)

class gui:
    @staticmethod   
    def image_resize(size, path):
        im = Image.open(path)
        im = im.resize(size)
        return ctk.CTkImage(im)

    @staticmethod
    def gui():
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        root = ctk.CTk()
        root.configure(bg='#353746')
        root.attributes('-fullscreen', True)
        root.title("Installer")

        frame = ctk.CTkFrame(root)
        frame.pack(side="top", fill='x', pady=20)

        brave_image = gui.image_resize((50, 50), "brave_icon.png")
        vscode_image = gui.image_resize((50, 50), "vscode_icon.png")
        zip_image = gui.image_resize((50, 50), "7zip_icon.png")
        filterkeysetter_image = gui.image_resize((50, 50), "filterkeysetter_icon.png")
        rainmeter_image = gui.image_resize((50, 50), "rainmeter_icon.png")

        brave_button = ctk.CTkButton(
            frame,
            text="Brave",
            command=downloads.start_brave,
            image=brave_image,
            compound="top",
            font=("Arial", 16, "bold"),
        )

        vscode_button = ctk.CTkButton(
            frame,
            text="VSCode",
            command=downloads.start_vscode,
            image=vscode_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        zip_button = ctk.CTkButton(
            frame,
            text="7-Zip",
            command=downloads.start_7zip,
            image=zip_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        filterkeysetter_button = ctk.CTkButton(
            frame,
            text="Keysetter",
            command=downloads.start_filterkeysetter,
            image=filterkeysetter_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        rainmeter_button = ctk.CTkButton(
            frame,
            text="Rainmeter",
            command=downloads.start_rainmeter,
            image=rainmeter_image,
            compound="top",
            font=("Arial", 16, "bold")
        )

        brave_button.pack(padx=20, pady=20, side="left")
        vscode_button.pack(padx=20, pady=20, side="left")
        zip_button.pack(padx=20, pady=20, side="left")
        filterkeysetter_button.pack(padx=20, pady=20, side="left")
        rainmeter_button.pack(padx=20, pady=20, side="left")

        root.mainloop()

if __name__ == "__main__":
    gui.gui()
