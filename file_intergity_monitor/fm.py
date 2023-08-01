'''
    This is a FILE INTEGRITY MONITOR. 
    An FIM is used to monitor files/directories and report if any changes have been made.
    Said changes can be in the following three forms:
        1) A change in contents of a file
        2) A file being deleted
        3) A new file being created

'''

import os
import sys
import time
import hashlib

# Used to create an image of file
def createImage(path):
    with open(path, 'rb') as fileContent:
        data = fileContent.read()
        return hashlib.sha512(data).hexdigest()

# Used to add new path to record
def addPathToRecord(dirName):
    # create a new directory named as the path
    os.mkdir(dirName)

# creates a new image of "absPath" and stores it in "imgPath"
def updateImage(imgPath, absPath):

    # delete image if it already exists
    imgPath = os.path.join(imgPath, "image.txt")
    if(os.path.exists(imgPath)):
        os.remove(imgPath)
    
    directory = os.listdir(absPath)
    count = 0
    for filename in directory:
        filePath = os.path.join(absPath, filename)
        image = createImage(filePath)
        with open(imgPath, 'a') as imgFile:
            imgFile.write(f"{filePath}::{image}\n")
        count+=1

    print(f"Image updated for {count} file(s)")


# For an existing path, create/compare image
def compareImage(imgPath, absPath):
    fileImages = {}
    imgPath = os.path.join(imgPath, 'image.txt')
    
    # store all images in a dictionary
    with open(imgPath, 'r') as imgFile:
        for line in imgFile:
            filePath, image = line.strip().split('::')
            print("Found in image:")
            print(f"{filePath}, {image}")
            fileImages[filePath] = image

    # continously check files
    while (True):
        
        files = os.listdir(absPath)

        # check for each file in the directory
        for f in files:
            fpath = os.path.join(absPath, f)
            fImage = createImage(fpath)

            # if image doesn't exist in dictionary, its a new file
            if fpath not in fileImages:
                print(f"{fpath} has been created")

            # if image is different than stored image, file has been changed
            elif fpath in fileImages and fileImages[fpath]!=fImage:
                print(f"{fpath} has been changed")

        # check for deleted files
        for existingFilePath in fileImages.keys():
            if os.path.exists(existingFilePath)==False:
                print(f"{existingFilePath} has been deleted")

        # to prevent continuous outputs when a change is detected
        time.sleep(1)

# Start of the main program

if(len(sys.argv)!=2 or sys.argv[1]=="-help" or sys.argv[1]=="-info"):
    
    # incorrect input/ show help menu
    print("Welcome to FILE INTEGRITY MONITOR")
    print("usage: fim.py <full_path>")

else:
    
    # path where all images are stored
    dataDir = "data"

    # correct path entered
    absPath = sys.argv[1]
    # pathDirName is the name of the directory where data regarding absPath is stored
    pathDirName = absPath.replace('\\', '_')
    
    
    # check if data regarding absPath already exists in records
    if(os.path.exists(pathDirName)==False):
        # data doesn't exist, create new record for path
        print("Path doesn't exist in record, adding path to record")
        addPathToRecord(pathDirName)

    print("Path exists in record")
    print("    (A) Update Image")
    print("    (B) Compare Image")
    choice = input("Enter one of A/B: ")
    
    if(choice.upper()=="A"):
        updateImage(pathDirName, absPath)
    elif(choice.upper()=="B"):
        compareImage(pathDirName, absPath)