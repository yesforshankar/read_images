#This is Advaith's first git commit
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def split_line(text):

    # split the text
    #print(text.splitlines())
    data = []
    datalines = text.splitlines()
    # for each word in the line:
    for word in datalines:
        words = word.split()
        if (word != ""):
            data.append(words)
            # print the word
            #print(word)
    return (data)
img = cv2.imread('image6.png')
text=pytesseract.image_to_string(img)
print(split_line(text))

