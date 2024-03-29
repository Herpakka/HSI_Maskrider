#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Feb 15, 2024 03:41:03 AM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import colorsys
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

import beta1
import HSI_model as model

_debug = True  # False to eliminate debug printing from callback functions.
h, h2, s, v, s2, v2 = 0, 0, 0, 0, 0, 0
file_path = ""


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = beta1.HSI(_top1)

    default_str = "0"
    default_num = 0
    _w1.HUE_scale1.set(default_num)
    _w1.HUE_scale2.set(default_num)
    _w1.Intensity_scale1.set(default_num)
    _w1.Intensity_scale2.set(default_num)
    _w1.Satuation_scale1.set(default_num)
    _w1.Satuation_scale2.set(default_num)

    _w1.HUE_entry1.insert(0, str(default_str))
    _w1.HUE_entry2.insert(0, str(default_str))
    _w1.Intensity_Entry1.insert(0, str(default_str))
    _w1.Intensity_Entry2.insert(0, str(default_str))
    _w1.Satuation_entry1.insert(0, str(default_str))
    _w1.Satuation_entry2.insert(0, str(default_str))

    root.mainloop()


def st_vartolen(*args):
    global h, _w1
    if _debug:
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    arg = _w1.HUE_entry1.get()  # Retrieve the value from HUE_entry1
    arg_int = int(float(arg))
    h = arg_int
    _w1.HUE_scale1.configure(from_=arg_int)
    _w1.HUE_scale2.configure(from_=arg_int)
    _w1.HUE_entry2.delete(0, tk.END)
    _w1.HUE_entry2.insert(0, str(arg_int))

def st_lentoval(*args):
    global h
    if _debug:
        print("beta1_support.h_value1")
        for arg in args:
            print("	another arg:", arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    h = arg_int
    _w1.HUE_entry1.delete(0, tk.END)  # Clear previous value
    _w1.HUE_entry1.insert(0, str(arg_int))  # Insert new value
    _w1.HUE_scale2.configure(from_=arg_int)
    _w1.HUE_entry2.delete(0, tk.END)  # Clear previous value
    _w1.HUE_entry2.insert(0, str(arg_int))
    # frame1(h, s, v)
    #frame3(h)
    image.realtime_mask()


def ed_lentoval(*args):
    global h2
    if _debug:
        print("beta1_support.h_value2")
        for arg in args:
            print(" hue end:", arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    h2 = arg_int
    _w1.HUE_entry2.delete(0, tk.END)
    _w1.HUE_entry2.insert(0, str(arg_int))
    # frame2(h2, s2, v2)
    frame4(h2)
    image.realtime_mask()


def sat_lentoval(*args):
    global s
    if _debug:
        for arg in args:
            print("satuation =", arg)
        sys.stdout.flush()
    arg_int = float(arg)
    args_float = "{:.3f}".format(arg_int)
    s = arg
    _w1.Satuation_entry1.delete(0, tk.END)
    _w1.Satuation_entry1.insert(0, str(args_float))
    # frame1(h, s, v)
    image.realtime_mask()


def sat2_lentoval(*args):
    global s2
    if _debug:
        for arg in args:
            print("satuation =", arg)
        sys.stdout.flush()
    arg_int = float(arg)
    args_float = "{:.3f}".format(arg_int)
    s2 = arg
    _w1.Satuation_entry2.delete(0, tk.END)
    _w1.Satuation_entry2.insert(0, str(args_float))
    # frame2(h2, s2, v2)
    image.realtime_mask()


def inten_lentoval(*args):
    global v
    if _debug:
        for arg in args:
            print("intensity =", arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    v = arg_int
    _w1.Intensity_Entry1.delete(0, tk.END)
    _w1.Intensity_Entry1.insert(0, str(arg_int))
    # frame1(h, s, v)
    image.realtime_mask()


def inten2_lentoval(*args):
    global v2
    if _debug:
        for arg in args:
            print("intensity =", arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    v2 = arg_int
    _w1.Intensity_Entry2.delete(0, tk.END)
    _w1.Intensity_Entry2.insert(0, str(arg_int))
    # frame2(h2, s2, v2)
    image.realtime_mask()


def frame1(h, s, v):
    s = float(s)
    rgb = colorsys.hsv_to_rgb(h / 360, s, v)
    if _debug:
        print("H = ", h, "S = ", s, "V = ", v)

    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    print("rgb = ", r, g, b)
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    print("HEX = ", hex_color)

    style_name = "HUE1pre.TFrame"
    style = ttk.Style()
    style.configure(style_name, background=hex_color)
    _w1.HUE1pre.configure(style=style_name)


def frame2(h, s, v):
    s = float(s)
    rgb = colorsys.hsv_to_rgb(h / 360, s, v)
    if _debug:
        print("H2 = ", h, "S = ", s, "V = ", v)
        print("rgb = ", rgb)
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    print("HEX = ", hex_color)



def frame3(h):
    rgb = colorsys.hsv_to_rgb(h / 360, 1, 255)
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    print("HEX3 = ", hex_color)



def frame4(h2):
    rgb = colorsys.hsv_to_rgb(h2 / 360, 1, 255)
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    print("HEX4 = ", hex_color)



class image:
    def import_img():
        global file_path
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")]
        )
        print(file_path)
        if file_path:
            # Open the image file
            path = model.process.get_relative_path(file_path)
            image = model.process.rgb_to_hsi(path)
            # image = model.process.rgb_to_hsi(path)

            # Get the original dimensions of the image
            original_height, original_width = model.process.get_shape()
            print(original_width, original_height)
            # original_width, original_height = image.size

            # Get the dimensions of TFrame1
            target_width, target_height = (
                _w1.TFrame1.winfo_width(),
                _w1.TFrame1.winfo_height(),
            )

            # Calculate the resizing factor for width and height
            width_ratio = target_width / original_width
            height_ratio = target_height / original_height

            # Use the smaller of the two ratios to maintain aspect ratio
            resize_ratio = min(width_ratio, height_ratio)

            # Calculate the new dimensions
            new_width = int(original_width * resize_ratio)
            new_height = int(original_height * resize_ratio)

            # Resize the image
            # image = image.resize((new_width, new_height))
            pil_image = Image.fromarray(image)
            image = pil_image.resize((new_width, new_height))

            # Convert the image to a PhotoImage object
            photo = ImageTk.PhotoImage(image)

            # Clear previous image if exists
            for widget in _w1.TFrame1.winfo_children():
                widget.destroy()

            # Display the image in a label
            label = tk.Label(_w1.TFrame1, image=photo)
            label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
            label.pack(fill="both", expand=True)

    def realtime_mask():
        path = model.process.get_relative_path(file_path)
        image = model.process.display_mask(path)
        # Get the original dimensions of the image
        original_height, original_width = model.process.get_shape()
        print(original_width, original_height)
        # original_width, original_height = image.size

        # Get the dimensions of TFrame1
        target_width, target_height = (
            _w1.TFrame1.winfo_width(),
            _w1.TFrame1.winfo_height(),
        )

        # Calculate the resizing factor for width and height
        width_ratio = target_width / original_width
        height_ratio = target_height / original_height

        # Use the smaller of the two ratios to maintain aspect ratio
        resize_ratio = min(width_ratio, height_ratio)

        # Calculate the new dimensions
        new_width = int(original_width * resize_ratio)
        new_height = int(original_height * resize_ratio)

        # Resize the image
        # image = image.resize((new_width, new_height))
        pil_image = Image.fromarray(image)
        image = pil_image.resize((new_width, new_height))

        # Convert the image to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Clear previous image if exists
        for widget in _w1.TFrame1.winfo_children():
            widget.destroy()

        # Display the image in a label
        label = tk.Label(_w1.TFrame1, image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        label.pack(fill="both", expand=True)


if __name__ == "__main__":
    beta1.start_up()
