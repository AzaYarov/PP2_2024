import os

path = os.getcwd()

if os.path.exists(path):
    print("Path exists")
    
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist")
