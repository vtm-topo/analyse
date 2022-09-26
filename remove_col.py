import glob
import os
from lxml import etree


files_list = glob.glob("/home/bilatli/DEV/DIGITAL-HUMANITIES/FRIGO/data/*.xml") #getting our list of XML files in our directory
#print(files_list)

#create folder for results
if not os.path.exists('results'):
    os.makedirs('results')

for file in files_list:
    filename = os.path.basename(file) #Retrieving the filename without the full path for saving the files at the end
    #print(filename)
    #print(file)
    tree = etree.parse(file) #parsing tree
    root = tree.getroot() #getting root
    #print(root)
    # Retrieving the id of the column that we want to delete
    for x in root[1]:
        #print(x.attrib)
        if x.attrib['LABEL'] == 'CustomLine:confins':
            id_confins = x.attrib['ID']
        elif x.attrib['LABEL'] == 'CustomLine:francs':
            id_francs = x.attrib['ID']
        elif x.attrib['LABEL'] == 'CustomLine:mutations':
            id_mutations = x.attrib['ID']
    #print('Confins:',id_confins,', ' 'francs:', id_francs,', ','mutations:', id_mutations)

    #Removing empty lines
    for t in root.iter('{*}TextLine'):
        for String in list(t):
            try:
                if String.attrib['CONTENT'] == "":
                    print(t.attrib['ID'], '--------','HAS BEEN REMOVED FROM FILE: ', file, '--------')
                    t.getparent().remove(t)
            except:
                continue

    #Removing the columns we want to get rid of. Here it is possible to comment out the .remove() method to keep a column.
    for t in root.iter('{*}TextLine'):
        try:
            if t.attrib['TAGREFS'] == id_confins:
                print('oyeah confins no remove')
                #t.getparent().remove(t)
            elif t.attrib['TAGREFS'] == id_mutations:
                t.getparent().remove(t)
            elif t.attrib['TAGREFS'] == id_francs:
                t.getparent().remove(t)
        except:
            print("An exception occurred. No TAGREFS at: ", t.attrib['ID'], " FILE: ", file)
            continue

    saving_file = "results/{}".format(filename) #We do not need to add the .xml, tree.write does this for us. We created the results directory in the beginning
    with open(saving_file, 'wb') as f:
        tree.write(f)
