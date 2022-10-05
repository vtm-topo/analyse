# Tools and analysis
This repo contains jupyter notebook and python files I used to prepare the data for feeding kraken (htr).

## Generating test.txt eval.txt and train.txt
It usually is common to use a script to randomly distribute the data between test, eval and train. A great explaination on the importance of data spliting with cute dogs and cats can be found [here](https://mlu-explain.github.io/train-test-validation/#intro)
However, sometimes we want to manually select the files for test and eval and leave the rest in train.
### [file-analysis.ipynb](https://github.com/vtm-topo/analyse/blob/main/files-analysis.ipynb)
A jupyter notebook to distribute the name of the files in test, eval and train, then save the distribution in txt files.

### [file-classification.ipynb](https://github.com/vtm-topo/analyse/blob/main/file-classification.ipynb)
Same as before, but we read the name of the files from the test.txt and eval.txt and train.txt is created with whatever files is left in our data directory.

## xml exploration and removing some lines based on type
I wanted to test if there are any differences in the recognition results if I remove the most complexe lines. In my case, it is mostly the "mutations"-> "CustomLine:mutations", but eventually also the "francs" -> "CustomLine:francs" and the "confins" -> "CustomLine:confins"
### [XML-parsing.ipynb](https://github.com/vtm-topo/analyse/blob/main/XML-parsing.ipynb)
The exploration with a jupyter notebook before directly writing a python script.
### [remove_col.py](https://github.com/vtm-topo/analyse/blob/main/remove_col.py)
The script to remove those lines on all xml files in a directory.


