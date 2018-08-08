import Tkinter as tk
import tkFileDialog

import fiberAlignment

from PIL import ImageTk, Image

"""
Dependencies: 
    cv2
    pillow
"""

def openImage():
    pass

def run():
    root = tk.Tk()
    root.geometry("1200x600")
    root.grid()

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    _file = tk.Menu(menubar)
    _file.add_command(label="Open Image", command=openImage)
    menubar.add_cascade(label="File", menu=_file)

    img = Image.open("percent4m.jpeg")
    img = img.resize((600, 600))

    imgtk = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=imgtk)
    label.grid(row=0, column=0)
    # canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
    root.mainloop()

if __name__=="__main__": run()
