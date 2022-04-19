# -*- coding: utf-8 -*-

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox

import pdf_gen

def ref():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir=iDir)
    path_text.set(iDirPath)

def run():
    try:
        pdf_gen.main(path_text.get())
    except FileNotFoundError:
        messagebox.showerror("ERROR", "パスを指定してください。")
        return
    messagebox.showinfo("INFO", "Execute complete!!")

root = tk.Tk()
root.title("pdf_gen")
root.geometry("310x50")
root.resizable(0, 0)

frame = ttk.Frame(root, padding=10)
# frame.pack(fill = tk.BOTH, padx=10, pady=10)
frame.grid()

path_text = tk.StringVar()
path_entry = tk.Entry(frame, textvariable=path_text, width=32)
path_entry.grid(row=0, column=0, padx=5, pady=5)
# src_path.place(x=10, y=10)

text_ref = tk.StringVar(frame)
text_ref.set('参照')
ref_path_button = tk.Button(frame, textvariable=text_ref, command=ref)
ref_path_button.grid(row=0, column=1, padx=5, pady=5)

text_run = tk.StringVar(frame)
text_run.set('実行')
exec_button = tk.Button(frame, textvariable=text_run, command=run)
exec_button.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
