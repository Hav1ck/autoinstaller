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
        