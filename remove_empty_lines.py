import glob
import os
from lxml import etree

'''This script removes empty line. Sometimes, ghost lines are created using eScriptorium.
With 0 width 0 height and no text, those remains invisible.
In that case, it might be good to use this script. Pay attention though that it will remove all empty lines and
most of the time, empty lines are just normal mistakes. The lines are actually visible.
We suggest to use this script while commenting out the saving part, in order to flag empty lines first.
Manually check if it is or not a ghost lines, correct the lines if possible and when you cannot do otherwise, use this script.'''

files_list = glob.glob("/home/bilatli/DEV/DIGITAL-HUMANITIES/CHABLE/data/*.xml") #getting our list of XML files in our directory

for file in files_list:
    tree = etree.parse(file) #parsing tree
    root = tree.getroot() #getting root


    #Removing empty lines
    for t in root.iter('{*}TextLine'):
        for String in list(t):
            try:
                if String.attrib['CONTENT'] == "":
                    print(t.attrib['ID'], '--------','HAS BEEN REMOVED FROM FILE: ', file, '--------')
                    t.getparent().remove(t)
            except:
                continue

    tree.write(file)
