import os
#use the os lib to run 'pip install -r requirements.txt' in the terminal
def install():
    return os.system("pip install -r requirements.txt")

def update():
    return os.system("pip install --upgrade -r requirements.txt")

