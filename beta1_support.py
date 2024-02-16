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

import beta1

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = beta1.HSI(_top1)
    root.mainloop()
def st_lentoval(*args):
    if _debug:
        print('beta1_support.h_value1')
        for arg in args:
            print ('	another arg:', arg)
        sys.stdout.flush()
    arg_int = int(float(arg))

    _w1.HUEstVal.delete(0, tk.END)  # Clear previous value
    _w1.HUEstVal.insert(0, str(arg_int))  # Insert new value
    _w1.HUEedLen.configure(from_=arg_int)
    _w1.HUEedVal.delete(0, tk.END) # Clear previous value
    _w1.HUEedVal.insert(0, str(arg_int))
def ed_lentoval(*args):
    if _debug:
        print('beta1_support.h_value2')
        for arg in args:
            print (' hue end:',arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    _w1.HUEedVal.delete(0, tk.END)
    _w1.HUEedVal.insert(0, str(arg_int))
def sat_lentoval(*args):
    if _debug:
        for arg in args:
            print("satuation =",arg)
        sys.stdout.flush()
    arg_int = float(arg)
    args_float = '{:.3f}'.format(arg_int)
    _w1.satVal.delete(0, tk.END)
    _w1.satVal.insert(0, str(args_float))
def inten_lentoval(*args):
    if _debug:
        for arg in args:
            print("intensity =",arg)
        sys.stdout.flush()
    arg_int = int(float(arg))
    _w1.intenVal.delete(0, tk.END)
    _w1.intenVal.insert(0, str(arg_int))

if __name__ == '__main__':
    beta1.start_up()




