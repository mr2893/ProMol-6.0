from pymol import cmd
from pymol import stored
import tkinter as tk
import Pmw
import os
import re
import time
import math
import tkinter.filedialog
from shutil import copy
from tkinter.filedialog import *
from tkinter.simpledialog import askstring
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter import *
from pmg_tk.startup.ProMol.treewidgets import widget, node, texttree
from pmg_tk.startup.ProMol.treewidgets.constants import *
import tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
import pmg_tk.startup.ProMol.load_csa_lit as lib
import pmg_tk.startup.ProMol.Methods.proutils as proutils
import pmg_tk.startup.ProMol.Methods.motifset as motifset
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
pdbsl = 0
Pmw.initialise()

#loads a PDB file from hard drive
#the custom file is added to multipdb textbox, saved to the PDBDownloads file, and read from there
def loadlocal(): 
    last_used_dir = glb.LAST_USED_DIR
    pdb = tkinter.filedialog.askopenfilename(filetypes = (("PDB files", "*.pdb"), \
                                       ("text files", "*.txt"), \
                                       ("all files", ".*")), \
                                       initialdir = last_used_dir, \
                                       multiple=False)
    if pdb and pdb is not None:
        glb.LAST_USED_DIR = os.path.dirname(pdb)
        try:
            copy(pdb, glb.FETCH_PATH)
            data = pdb.split("/")
            name = data[len(data) - 1].split(".")[0]
            #name += ', '
            glb.GUI.motifs['multipdb'].insert(END, name) 
            print("Loaded local file " + pdb)
        except: 
            showerror("Open Source File", "Failed to read file \n'%s'"%pdb)
            return

#clears all input from the multipdb texbox
def clearpdbinput():
    glb.GUI.motifs['multipdb'].delete(1.0, END)    
# cdb 3/31/15
# takes a file consisting of 1 list of pdbids at one pdbid on each line and uploads 
# it into the entry box  
def askopenfilename():

        fileoptions = {}
        fileoptions['defaultextension'] = '.txt'
        fileoptions['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        fileoptions['initialdir'] = 'C:\\'
        fileoptions['initialfile'] = ''
        fileoptions['title'] = 'Select a file of proteins'

        filename = tkinter.filedialog.askopenfilename(**fileoptions)
    
        if filename and filename is not None:
            fo = open(filename, 'r')
        
            query = ""
            linecount = 0
            for line in fo:
                linecount += 1;
                coden = "";
                # Strip leading blanks
                line = line.lstrip();
                # Strip trailing blanks and newlines
                line = line.strip().replace('\n','')
                for c in line:
                    if c.isalnum():
                        coden+=c
                    if (len(coden) > 3):
                         break
                if len(coden) is not 0:
                        query+= coden + ", "

            #account for empty files
            if linecount > 1:
                query = query[:-2]
        
            fo.close()
            glb.GUI.motifs['multipdb'].insert(END,query)
