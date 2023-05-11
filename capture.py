'''
from pikepdf import Pdf,Name,PdfImage

old_pdf=Pdf.open('document.pdf')
page_1=old_pdf.pages[0]

print(list(page_1.images.keys()))
x=list(page_1.images.keys())

raw_image=page_1.images[x[0]]
pdf_image=  PdfImage(raw_image)

pdf_image.extract_to(fileprefix='text1')

'''


# Need these libraries
# pip install keyboard
# pip install PyAutoGUI
# pip install python-docx
# pip install win32gui

import keyboard
import pyautogui
from docx import Document
from docx.shared import Inches
import win32gui
from PIL import ImageGrab

shotfile = "C:/tmp/shot.png"  # temporary image storage 
docxfile = "C:/tmp/shots.docx" # main document
hotkey = 'ctrl+shift+q'  # use this combination anytime while script is running

def do_cap():
    try:
        print ('Storing capture...')
        
        hwnd = win32gui.GetForegroundWindow()  # active window
        bbox = win32gui.GetWindowRect(hwnd)  # bounding rectangle

        # capture screen
        shot = pyautogui.screenshot(region=bbox) # take screenshot, active app
        # shot = pyautogui.screenshot() # take screenshot full screen
        shot.save(shotfile) # save screenshot
        
        # append to document. Doc must exist.
        doc = Document(docxfile) # open document
        doc.add_picture(shotfile, width=Inches(7))  # add image, 7 inches wide
        doc.save(docxfile)  # update document
        print ('Done capture.')
    except Exception as e:  # allow program to keep running
        print("Capture Error:", e)

keyboard.add_hotkey(hotkey, do_cap)  # set hot keys

print("Started. Waiting for", hotkey)

keyboard.wait()   # Block forever