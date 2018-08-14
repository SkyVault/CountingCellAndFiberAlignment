import Tkinter as tk
import tkFileDialog
import cv2
import numpy as np
import math
import matplotlib

from fiberAlignment import FiberAlignment
from cell_counter import CellCounter

from PIL import ImageTk, Image

FILTERS = {
        "FiberAlignment": FiberAlignment,
        "CellCounter": CellCounter
}

"""
Dependencies: 
    cv2
    pillow
"""

class Application():
    def __init__(self, size):
        self.inImgData = None
        self.outImgData = None

        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(size[0], size[1]))

        self.inLabel = tk.Label(self.root, text="")
        self.outLabel = tk.Label(self.root, text="")
        self.inLabel.pack(side="left")
        self.outLabel.pack(side="left")

        # Menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self._file = tk.Menu(self.menubar)
        self._file.add_command(label="Open Image", command=self.openImage)
        self.menubar.add_cascade(label="File", menu=self._file)

        self.BottomFrame = tk.Frame(self.root) 
        self.BottomFrame.pack(side="bottom")

        self.button = tk.Button(self.BottomFrame, text="Generate", command=self.applyFilter)
        self.button.pack(side="left")

        self.genTypeStringVar = tk.StringVar(self.root)
        self.genTypeStringVar.set(next(iter(FILTERS)))

        self.popdownMenu = tk.OptionMenu(self.BottomFrame, self.genTypeStringVar, *FILTERS)
        self.popdownMenu.pack(side="right")

        self.root.mainloop()

    def applyFilter(self):
        result = FiberAlignment(self.inLabel.path)
        self.outImgData = Image.fromarray(np.uint8(result))

        imgtk = ImageTk.PhotoImage(self.outImgData)

        self.outLabel.config(image=imgtk)
        self.outLabel.imgtk = imgtk
        
        self.inLabel.pack_forget()
        self.inLabel.pack(side="left")

        self.outLabel.pack_forget()
        self.outLabel.pack(side="right")

    def openImage(self):
        result = tkFileDialog.askopenfilename(
                initialdir="", 
                title="Select Image", 
                filetypes=(("Jpeg files", "*.jpg *.jpeg"), ("Png files", "*.png"), ("all files", "*.*")))

        if result:
            self.inImgData = Image.open(result)
            self.inImgData = self.inImgData.resize((600, 600))

            imgtk = ImageTk.PhotoImage(self.inImgData)

            self.inLabel.config(image=imgtk)
            self.inLabel.imgtk = imgtk
            self.inLabel.path = result
            self.inLabel.pack_forget()
            self.inLabel.pack()

def run():
    Application((1200, 600))

if __name__=="__main__": run()
