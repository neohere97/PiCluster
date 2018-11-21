# Spawn the fileServer
# Spawn a web server
# spawn the excecute.py

import threading
import os
import sys
from subprocess import call
from multiprocessing import *

current_working_directory = os.path.dirname(sys.argv[0])

def launch_file_server():
    os.chdir(f"{current_working_directory}/ToolsDirectory")
    call(["python3","-m","http.server"])
def launch_web_server():

def printit():
  print(current_working_directory)
  threading.Timer(5.0, printit).start() 
  
    
launch_fileServer() 






