# Documentation for automating file/folder sorting

## Order of executing script

The scipt is excuted by changing directory into auto_group and executing **python determine_location.py**.
This will ask a number of questions regarding the directory you want file executed into. 


This execution will call on the a function within the module **gather_files.py** called  then call on the module **type_of_file.py**.
The code in type_of_file will return a dictionary of the file ending and list of how to to perhaps sort it in a defualt way. 


## installation
There are 2 methods to install and use this script and the method you choose will determine which branch you will need to work from. 
There two methods of installation is either : 
1. Using **pip**
2. Using **git clone**

###  Install with PIP
If you are using the command line, then within your command line or terminal, first install python3, python-pip and then run the command

```
pip install sortmyfolder
```

After which you should then provide the path of the directory you want to sort and then run

```
sortmyfolder --location <PathOfYourChoice>
```


### Installation with git clone 
If you are using the git clone option, please only use the **main** branch

Begin with : -
1. ``` git clone https://gitlab.com/emmanuelagyapong/auto_group.git ```
2. change directory with ``` cd auto_group ```
3. then run ```python3 determine_location.py <PathOfYourChoice> ```


### Important
You will need to put an evironment variable in place for the module to work effectively. 
As shown below, however you need to find the location of where your python packages are installed and add your site-packages as shown in the example below.


 ```export PYTHONPATH="{PYTHONPATH}:/Users/emmanuelagyapong/Desktop/veloxci/env/lib/python3.9/site-packages/auto_group"```

