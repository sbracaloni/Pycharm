PyCharm Python Dev Environment
==============================

---

Needed resources
----------------

- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC) 
- virtualenv

> Note this tutorial is elaborated on Ubuntu 18.04
---

Install PyCharm
----------------   

    mkdir ~/pycharm
    tar xzvf ~/Downloads/pycharm-community-*.tar.gz -C ~/pycharm/
     ~/pycharm//pycharm-community-*/bin/pycharm.sh
----
![alt text](./images/install_pycharm/install1.png "Install popup 1.")
----
![alt text](./images/install_pycharm/install2.png "Install popup 2.")
----
![alt text](./images/install_pycharm/install3.png "Install popup 3.")
----
![alt text](./images/install_pycharm/install4.png "Install popup 4.")
----
![alt text](./images/start.png "End of install. Start popup.")
---

Install Virtualenv
------------------

    sudo apt-get install virtualenv
    
---

Create a New Project
-----------------------

![alt text](./images/start.png "Start popup.")

Click on **+ Create New Project**

----
![alt text](./images/new_prj/new_prj1.png "New project popup 1.")
Set the **Location** path && Create a new **virtualenv**

----
![alt text](./images/new_prj/new_prj2.png "New project popup 2.")
The Project is Created. 

----
Display the Toolbar:
![alt text](./images/new_prj/new_prj7.png "Display the toolbar.")

----
### Create a New Python File

    => Right click on prj1 
           => New
                => Python File
![alt text](./images/new_prj/new_prj4.png "New python file.")

----
Use name **"my_script"** (the .py extension is automatically added for Python Files) 
![alt text](./images/new_prj/new_prj5.png "New python file select name.")

----

Python file : **my_script.py** is created
![alt text](./images/new_prj/new_prj6.png "New python file select name.")

----
### Run The Script

    Right click inside the script (or on teh file name)
        => Run 'my_script'
        
![alt text](./images/new_prj/new_prj8.png "Run script")

----
![alt text](./images/new_prj/new_prj10.png "Execution result")

----
![alt text](./images/new_prj/new_prj9.png "Project structure")

----
### Close The Project

    File 
      => Close Project

Then now **prj1** is in quick access in the main page.
![alt text](./images/new_prj/new_prj11.png "Run script.")

---

Import an existing project
--------------------------


Download [sources](https://drive.google.com/file/d/1EMRsLkobZ-WtfZd69kMiqkaouPL3fgmA/view?usp=sharing) 
and extract them

![alt text](./images/prj2/prj2_1.png "Sources")

----
Create a *virtualenv* then activate it

        cd [extracted source directory]
        virtualenv venv -p /usr/bin/python3
        . ./venv/bin/activate

![alt text](./images/prj2/prj2_2.png "Venv activated")

----
Open the project in *Pycharm*:
- From the main page: click on **Open**
- From an opened project: click on **File => Open**

![alt text](./images/prj2/prj2_3.png "Loaded Project")

----
Run *my_script.py*

**Error :**  ModuleNotFoundError: No module named 'yaml'
![alt text](./images/prj2/prj2_4.png "Module not found error")

----
See /my_lib/loader/specific/yaml_loader.py

![alt text](./images/prj2/prj2_5.png "import yaml")       

----

A module is missing. All needed project modules should be specified
in a `requirement.txt` file.

Install requirement in current virtual env using `requirement.txt`:

![alt text](./images/prj2/prj2_6.png "Install requirements")
    
 
----
Run *my_script.py*

Everything works!

---


Import an existing project - Case 2
-------------------------------------


1. Download [sources](https://drive.google.com/file/d/1ZJdzXBNrmdYjxNSKxzMM7TeoNp9fRnmA/view?usp=sharing) 
and extract them

2. Create a *virtualenv* then activate it

        cd [extracted source directory]
        virtualenv venv -p /usr/bin/python3
        . ./venv/bin/activate

3. Open the project in *Pycharm*:
    - From the main page: click on **Open**
    - From an opened project: click on **File => Open**

----
![alt text](./images/prj3/prj3_1.png "Project loaded")

----

There is import errors, but **HowOldAreYouPlugin** exists in 
    *various/python/plugin/display/how_old.py*

![alt text](./images/prj3/prj3_4.png "Import errors")

----
### Set The Project Structure


- Open Settings

![alt text](./images/prj3/prj3_5.png "Open settings")

----

- Select **Project: prj3**

![alt text](./images/prj3/prj3_3.png "Open settings")

----

- Check if the interpreter is the right one.

![alt text](./images/prj3/prj3_2.png "Open settings")

----
- Set the project structure

The **Python structure** must be set to declare which directories are **Python modules**.
It has a direct impact on **Python imports**.
 
Helper: See [python import example](https://drive.google.com/file/d/1Bj3M-XdiQwmRF2vw9X4BLwlZupF4qECa/view?usp=sharing)
   
----
- Select a source directory. 

It must be the first parent of the top python module.Apply then Ok.

![alt text](./images/prj3/prj3_6.png "Select source directory")

----
![alt text](./images/prj3/prj3_7.png "Almost resolved")

----

Plugin imports seem to be resolved but they are remaining issues with helpers.
Find the solution without modifying imports in source files.

---

Existing Project With Tests
---------------------------


1. Download [sources](https://drive.google.com/file/d/1wIZYRVbMfCooZhJ6m0wdVoUFzhIXhrCx/view?usp=sharing) 
and extract them

2. Create a *virtualenv* then activate it

        cd [extracted source directory]
        virtualenv venv -p /usr/bin/python3
        . ./venv/bin/activate

3. Open the project in *Pycharm*:
    - From the main page: click on **Open**
    - From an opened project: click on **File => Open**

----
![alt text](./images/prj4/prj4_a1.png "Project loaded")

----
### Setup test runner

Open **Settings** then search 'test'
![alt text](./images/prj4/prj4_a2.png "Setting search")
----

In **Python Integrated Tools** set **pytest** as *Default test runner*
![alt text](./images/prj4/prj4_a3.png "Set pytest")

----
Run tests

    Right click on file name => Run 'pytest in test_find_...'

![alt text](./images/prj4/prj4_a4.png "Run tests")

----
The tests fail! 

    It also possible to run one test function:
        Right click on test function => Run ...
    
----
### Use the debugger

Add a breakpoint in the first test (line 9)

![alt text](./images/prj4/prj4_5.png "Add breakpoint")


----
Run in debug mode.

    The whole file: 
     Right click on file name => Debug 'pytest in ...'
    
    A function: 
     Right click inside the function =>  Debug 'pytest in ...'
    
----
Click on the icon which seems to be glasses in the middle of the debug section.

![alt text](./images/prj4/prj4_4.png "Start debugger")

----

| Left  | Middle   | Right |
|---|---|---|
|execution stack | current variables | inspector |
![alt text](./images/prj4/prj4_3.png "Display watcher")

----
Step Over the statement

![alt text](./images/prj4/prj4_2.png "Step over")

----
Step Into the function

![alt text](./images/prj4/prj4_2.png "Step into")

----
You can inspect expression
![alt text](./images/prj4/prj4_1.png "Step into")
----
![alt text](./images/prj4/prj4_b1.png "Step into")
----
 Use the debugger to fix the code!
 All tests must succeed.