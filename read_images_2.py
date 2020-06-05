#This is Advaith's first git commit
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import matplotlib.pyplot as plt
import numpy as np
import itertools

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

dataout=[]
dataout=split_line(text)
print(dataout)
list_lang,list_male,list_female,list_total = map(list, zip(*dataout))
del(list_lang[-1])
del(list_male[-1])
del(list_female[-1])
del(list_total[-1])
i=0
# for item in itertools.chain(list_male, list_female):
#     # Do something with each list item
#     sizes_gender.append(list_male[i])
#     sizes_gender.append(list_female[i])
#     i=i+1

# print(sizes_gender)
 
# Data to plot
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()