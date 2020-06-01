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

print(list_lang)
print(list_male)
print(list_female)
print(list_total)

i=0
for item in itertools.chain(list_male, list_female):
    # Do something with each list item
    sizes_gender.append(list_male[i])
    sizes_gender.append(list_female[i])
    i=i+1

print(sizes_gender)
 
# Data to plot
labels = list_lang
sizes = list_total
labels_gender = ['Male', 'Female']*len(list_male)
sizes_gender = [*list_male,*list_female]
print(len(list_female))
print(labels_gender)
print(sizes_gender)
colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff']
colors_gender = ['#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
explode = (0,0,0,0) 
explode_gender = (0,0,0,0,0,0,0,0)
#Plot
texts=plt.pie(sizes, labels=labels, colors=colors, startangle=90,frame=True, explode=explode,radius=3)
autotexts=plt.pie(sizes_gender,labels=labels_gender, colors=colors_gender,startangle=90, explode=explode_gender,radius=2 )


#Draw circle
centre_circle = plt.Circle((0,0),1.5,color='black', fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 
plt.axis('equal')
plt.tight_layout()
plt.show()