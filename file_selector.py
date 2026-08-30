import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp"),
                                                      ("All Files", "*.*")
                                                      ]
                                            )

    root.destroy()
    
    return file_path