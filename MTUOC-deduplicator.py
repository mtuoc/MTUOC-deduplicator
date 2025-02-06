#    MTUOC-deduplicator
#    Copyright (C) 2025  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Segmentation is performed using srx_segmenter: https://github.com/narusemotoki/srx_segmenter
#    The code is copied into this script.

import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import itertools
import codecs

def select_input_file():
    infile = askopenfilename(initialdir = ".",filetypes =(("txt files","*.txt"),("All Files","*.*")),
                           title = "Select the input file.")
    E1.delete(0,END)
    E1.insert(0,infile)
    E1.xview_moveto(1)
    
def select_output_file():
    infile = asksaveasfilename(initialdir = ".",filetypes =(("txt files","*.txt"),("All Files","*.*")),
                           title = "Select the output file.")
    E2.delete(0,END)
    E2.insert(0,infile)
    E2.xview_moveto(1)
    
def go():
    
    infilename=E1.get()
    outfilename=E2.get()
    outfile=codecs.open(outfilename,"w",encoding="utf-8")
    with open(infilename, "r", encoding = "utf-8") as infile:
        sorted_file = sorted(infile.readlines())
    for line, _ in itertools.groupby(sorted_file):
        outfile.write(line)

top = Tk()
top.title("MTUOC-deduplicator")

B1=tkinter.Button(top, text = str("Select input file"), borderwidth = 1, command=select_input_file,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=60, justify="right")
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Select output file"), borderwidth = 1, command=select_output_file,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=60, justify="right")
E2.grid(row=1,column=1)

B2=tkinter.Button(top, text = str("Deduplicate!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=3,column=0)

top.mainloop()
    







