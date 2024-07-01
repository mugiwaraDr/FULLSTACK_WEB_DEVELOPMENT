Follow these steps 
1. Install the Python extension.- Open VS Code IDE and click extensions there 
automatically u will be shown Python extension (Make sure you are connected 
to Internet) 
2. On your file system, create a project folder 
3. In that folder, use the following command (as appropriate to your computer) 
to create a virtual environment named env based on your current interpreter: 
# Windows 
**python -m venv env **
4. Open the project folder in VS Code by running code ., or by running VS Code 
and using the File > Open Folder command. 
5. In VS Code, open the Command Palette (View > Command Palette or 
**(Ctrl+Shift+P)).** Then select the Python: Select Interpreter command:
6. The command presents a list of available interpreters that VS Code can locate 
automatically (your list will vary; if you don't see the desired interpreter, see 
Configuring Python environments). From the list, select the virtual environment 
in your project folder that starts with ./env or .\env: 
7. Create a New Terminal : In Menu Terminal -> New Terminal option 
Creating project: 
1. Create a django project - 
Type following command in the terminal opened: 
django-admin startproject p . 
(dot following project name is important which refers to current directory) 
This startproject command assumes (by use of . at the end) that the current 
folder is your project folder, and creates the following within it: 
● manage.py: The Django command-line administrative utility for the project. 
You run administrative commands for the project using python manage.py 
<command> [options]. 
● A subfolder named p which contains the following files: 
o     init .py: an empty file that tells Python that this folder is a Python 
package. 
o wsgi.py: an entry point for WSGI-compatible web servers to serve your 
project. You typically leave this file as-is as it provides the hooks for 
production web servers. 
o settings.py: contains settings for Django project, which you modify in 
the course of developing a web app. 
o urls.py: contains a table of contents for the Django project, which you 
also modify in the course of development. 
2. To verify the Django project, make sure your virtual environment is activated, 
then start Django's development server using the command python manage.py runserver. The server runs on the default 
port 8000, and you see output like the following output in the terminal 
window: 
Verify server by typing: 
**python manage.py runserver**
3. When you're done, close the browser window and stop the server in VS 
Code using Ctrl+C as indicated in the terminal output window. 
4. In the VS Code Terminal with your virtual environment activated, run the 
administrative utility's startapp command in  your  project  folder (where 
manage.py resides): 
**python manage.py startapp lab1 **
5. The command creates a folder called lab1 that contains a number of code 
files and one subfolder. Of these, you frequently work with views.py (that 
contains   the   functions   that   define    pages    in    your    web    app) and 
models.py (that  contains  classes   defining   your   data   objects). The 
migrations folder is used by Django's administrative utility to manage 
database  versions.  There  are  also  the  files apps.py (app configuration), 
admin.py (for  creating  an  administrative   interface), and tests.py (for 
unit tests).
