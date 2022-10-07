# Tools and analysis
This repo contains jupyter notebook and python files I used to prepare the data for feeding kraken (htr).

## Generating test.txt eval.txt and train.txt
It usually is common to use a script to randomly distribute the data between test, eval and train. A great explaination on the importance of data spliting with cute dogs and cats can be found [here](https://mlu-explain.github.io/train-test-validation/#intro)
However, sometimes we want to manually select the files for test and eval and leave the rest in train.

### [file-analysis.ipynb](https://github.com/vtm-topo/analyse/blob/main/files-analysis.ipynb)
A jupyter notebook to distribute the name of the files in test, eval and train, then save the distribution in txt files.
### [file-classification.ipynb](https://github.com/vtm-topo/analyse/blob/main/file-classification.ipynb)
Same as before, but we read the name of the files from the test.txt and eval.txt. train.txt is created with whatever files is left in our data directory.

### [dump-file-SEG.ipynb](https://github.com/vtm-topo/analyse/blob/main/dump-file-SEG.ipynb)
Same as before but for segmentation as the data can be slightly different between the two. We sometimes want to add files from other project for the htr but not for the segmentation part.

## xml exploration and removing some lines based on type
I wanted to test if there are any differences in the recognition results if I remove the most complexe lines. In my case, it is mostly the "mutations"-> "CustomLine:mutations", but eventually also the "francs" -> "CustomLine:francs" and the "confins" -> "CustomLine:confins"
I wrote a small script to remove lines based on type.

### [XML-parsing.ipynb](https://github.com/vtm-topo/analyse/blob/main/XML-parsing.ipynb)
The exploration with a jupyter notebook before directly writing a python script.
### [remove_col.py](https://github.com/vtm-topo/analyse/blob/main/remove_col.py)
The script to remove those lines on all xml files in a directory.

## [remove empty lines](https://github.com/vtm-topo/analyse/blob/main/remove_empty_lines.py)
Sometimes, ghost lines are created using eScriptorium.
With 0 width 0 height and no text, those remains invisible.
In that case, it might be good to use this script. Pay attention though that it will remove all empty lines and
most of the time, empty lines are just normal mistakes. The lines are actually visible.
We suggest to use this script while commenting out the saving part, in order to flag empty lines first.
Manually check if it is or not a ghost lines, correct the lines if possible and when you cannot do otherwise, use this script.

## remove empty zone
As for the lines, empty zone are sometimes created using eScriptorium. If they are big enough, we can see them and delete them. However, empty zones can be hard to locate even while zooming very close in the page. They are flaged by the htr-united githubaction though, telling us which files contains faulty zone. We can use the same technique that is used to find them but this time to delete them.

### [huntingEmptyZone.ipynb](https://github.com/vtm-topo/analyse/blob/main/huntingEmptyZone.ipynb)
The exploration with a jupyter notebook before directly writing a python script.
### [remove_empty_zone.py](https://github.com/vtm-topo/analyse/blob/main/remove_empty_zone.py)
The script to remove all empty zones on all files in a directory

## Finding xx marking difficulties in annotation
While annotating, some words are harder to read than other. I sometimes marked them by xx XX or more X with the intent to check them later and correct the transcription. It is a rather common way to work but it can also create dirt in our data if one forgets to correct those xx marked words. I wanted to see if a forgot to correct some words and if yes how many on which file.

### [finding-xxx.ipynb](https://github.com/vtm-topo/analyse/blob/main/finding-xxx.ipynb)
The exploration with a jupyter notebook before directly writing a python script.
### [flagxx.py](https://github.com/vtm-topo/analyse/blob/main/flagxx.py)
This script gives all files containing two xx following each other in the transcription and how many times they occur.



