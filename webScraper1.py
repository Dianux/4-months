
'''urlllib contains functions for requesting data across the web, handling cookies and changing metadata such as headers, etc.'''
#urlopen-used to open a remote object across a network and read it



from urllib.request import urlopen
import json

URL_request = urlopen(input("Type the cnn URL for Asia, where you'll find the word 'Korea': " )).read()



#open a file for writing

 # File requester
from tkinter import filedialog
from tkinter import *
root = Tk()
root.fileName = filedialog.askopenfilename(filetypes = ( ("txt","*.txt"), ("All files", "*.*")))


root.title(root.fileName)

#save text file to read



file_name = txt.writer(open('webScraper1', 'a', newline='')) #newline=',' allows python to handle rows and newlines.




#  open file to read

with open(root.fileName) as myFile:
    myFile = csv.reader(myFile, delimiter=',')
# pass file to csv reader
    next(myFile)
