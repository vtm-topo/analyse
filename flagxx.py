import glob
import os
import re
from lxml import etree

#files_list = glob.glob("/home/bilatli/DEV/DIGITAL-HUMANITIES/CHABLE/data/*.xml") #getting our list of XML files in our directory
files_list = glob.glob("/home/bilatli/DEV/DIGITAL-HUMANITIES/HTR-united/lectaurep-repertoires/data/lectaurep-random-set-1/*.xml")

for file in files_list:
    tree = etree.parse(file) #parsing tree
    root = tree.getroot() #getting root

    y = 0

    for t in root.iter('{*}TextLine'):
        for String in list(t):
            try:
                x = String.attrib['CONTENT']

                if re.search('x{2,}|X{2,}', x):
                    y = y+1
                    #print('XXXX found OMG!')
                    #print(x)
                else:
                    #print('Nope')
                    continue
            except:
                continue

    if y != 0:
        print(file,'contains ', y, 'xx')
