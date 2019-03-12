# Verify contents of the .tar generated after build

## Description

Python script which will take a text file with list of expected files and a tar file which is to be cross verified with the list, as a input and will return details about comparison of files present in .tar and .txt files. 

## Example

### Syntax
> python file-helper.py --text \<text-filesname\> --tar \<tar-filename\>

### Output
This script will return following output:
```
<status if all the files in .txt are present in given .tar file>

Expected file count: <total files in .txt>
Files from list that are present in .tar: <files which are in listed .txt and also available in .tar>
Extra files present in .tar : <files which are not listed .txt, but present in .tar>
```

### Tests
For testing purpose, I have included `filename_list.txt` and `test-1.tar`, `test-2.tar`.

This `.tar` files contains [publicly available test image data set by SIPI, University of Souther California](http://sipi.usc.edu/database/database.php?volume=textures).

`test-1.tar` contains all and only files that are listed in `filename_list.txt`, wheras `test-2.tar` contains some files that are listed in `filename_list.txt` and some addition files.