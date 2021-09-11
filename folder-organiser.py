## Any questions -> bas@taylorgraceac.co.uk

from genericpath import isdir
import time
import os
import shutil
from os import listdir
from os.path import isfile, join
from shutil import move
from distutils.dir_util import copy_tree

## PATHS

while True:
    def copytree(src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)


    initial_path = ('X:\Shared Files\Emails')
    final_path = ('X:')
    identification_path = ('Emails')

    directories_list = [f for f in listdir(initial_path) if isdir(join(initial_path, f))]

    for f in directories_list: 
        email_copy = f  ### I need to assign the filename to a variable, so that then I can reference it for copying
        project_number = f[14:18] ### I need to get the 4 digit project number
        project_number_str = str(project_number) ### I need to convert the project number into a str so that I can find such string in the folder
        general_folder_string = ("Q" + project_number[0] + project_number[1] + "00" + " - " + "Q" + project_number[0] + project_number[1] + "99") ### I create the General Folder String Q4700 - Q4799
        general_folder_path = os.path.join(final_path, general_folder_string) ### I make a path with the General Folder String
        specific_folder_directory = [f for f in listdir(general_folder_path) if isdir(join(general_folder_path, f))] ### Makes a list of all the folders in the General Folder Directory
        for f in specific_folder_directory: ### This function checks if the string taken from the file corresponds with any folder in the directory
            if project_number_str in f:
                pasting_path = os.path.join(general_folder_path, f, identification_path) ### If it corresponds, then join it and make a path named pasting_path
        copying_path = os.path.join(initial_path,email_copy) ### Make a path from where the file is copied, joining the initial path and the file in question
        shutil.move(copying_path,pasting_path) ### Copy the file to the project folder
        print(copying_path) ### Print the files that have been copied

    initial_path = ('X:\Shared Files\Quotes')
    final_path = ('X:')
    identification_path = ('Quotes')

    directories_list = [f for f in listdir(initial_path) if isdir(join(initial_path, f))]

    for f in directories_list: 
        email_copy = f  ### I need to assign the filename to a variable, so that then I can reference it for copying
        project_number = f[14:18] ### I need to get the 4 digit project number
        project_number_str = str(project_number) ### I need to convert the project number into a str so that I can find such string in the folder
        general_folder_string = ("Q" + project_number[0] + project_number[1] + "00" + " - " + "Q" + project_number[0] + project_number[1] + "99") ### I create the General Folder String Q4700 - Q4799
        general_folder_path = os.path.join(final_path, general_folder_string) ### I make a path with the General Folder String
        specific_folder_directory = [f for f in listdir(general_folder_path) if isdir(join(general_folder_path, f))] ### Makes a list of all the folders in the General Folder Directory
        for f in specific_folder_directory: ### This function checks if the string taken from the file corresponds with any folder in the directory
            if project_number_str in f:
                pasting_path = os.path.join(general_folder_path, f, identification_path) ### If it corresponds, then join it and make a path named pasting_path
        copying_path = os.path.join(initial_path,email_copy) ### Make a path from where the file is copied, joining the initial path and the file in question
        shutil.move(copying_path,pasting_path) ### Copy the file to the project folder
        print(copying_path) ### Print the files that have been copied
    time.sleep(300)
