from PIL import Image
import customtkinter as ctk

class Utils:
    @staticmethod
    def image_resize(size, path):
        im = Image.open(path)
        im = im.resize(size)
        return ctk.CTkImage(im)
