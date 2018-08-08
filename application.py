import Tkinter as tk
import tkFileDialog

import fiberAlignment

from PIL import ImageTk, Image

"""
Dependencies: 
    cv2
    pillow
"""

class Application():
    def __init__(self, size):
        self.inImgData = None

        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(size[0], size[1]))

        self.inLabel = tk.Label(self.root, text="No Image")

        # Menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self._file = tk.Menu(self.menubar)
        self._file.add_command(label="Open Image", command=self.openImage)
        self.menubar.add_cascade(label="File", menu=self._file)

        self.root.mainloop()

    def openImage(self):
        result = tkFileDialog.askopenfilename(initialdir="", title="Select Image", filetypes=(("Jpeg files", "*.jpg *.jpeg"), ("Png files", "*.png"), ("all files", "*.*")))
        if result:
            self.inImgData = Image.open(result)
            self.inImgData = self.inImgData.resize((600, 600))

            imgtk = ImageTk.PhotoImage(self.inImgData)

            self.inLabel.config(image=imgtk)
            self.inLabel.imgtk = imgtk
            self.inLabel.pack_forget()
            self.inLabel.pack()
        
def run():
    Application((1200, 600))

if __name__=="__main__": run()
