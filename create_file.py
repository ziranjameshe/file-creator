#!/usr/bin/python3

import argparse
import os
import sys
import getpass
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("file_type", choices = ['python', 'c', 'bash'], help = "Provide file type")

parser.add_argument("file_name", help = "Provide file name")

parser.add_argument("-m", "--mode", choices = ['744', '644'], default = '744', help = "Provide file permission. This is mainly for python files.")

args = parser.parse_args()


# Check if file already exists
cwd       = os.getcwd()

file_name =  cwd + '/' + args.file_name

if os.path.isfile(file_name):

    sys.exit('File already exits!')


def write_python_file(file_name):
    '''Write python file'''

    file_content = "#!/usr/bin/env ipython3\n\n"

    # getpass.getuser() returns the user name for the current user
    file_content += "# Author : %s\n\n"%getpass.getuser()

    file_content += "# Date   : %s\n\n" %datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(file_name, "w") as file:

        file.write(file_content)

    os.chmod(file_name, int(args.mode, base = 8))

def write_c_file(file_name):
    '''Write c file'''

    file_content = "/*\n"

    # getpass.getuser() returns the user name for the current user
    file_content += "Author : %s\n\n"%getpass.getuser()

    file_content += "Date   : %s\n" %datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    file_content += "*/\n"

    with open(file_name, "w") as file:

        file.write(file_content)

def write_bash_file(file_name):
    '''Write bash file'''

    file_content = "#!/usr/bin/bash\n\n"

    # getpass.getuser() returns the user name for the current user
    file_content += "# Author : %s\n\n"%getpass.getuser()

    file_content += "# Date   : %s\n\n" %datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(file_name, "w") as file:

        file.write(file_content)

    os.chmod(file_name, int('744', base = 8))
    


if __name__ == "__main__":

    if args.file_type == 'python':
        
        write_python_file(file_name)

    elif args.file_type == 'c':

        write_c_file(file_name)

    elif args.file_type == 'bash':

        write_bash_file(file_name)



