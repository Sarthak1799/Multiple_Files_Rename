import os

folderpath = input("Enter the correct path for folder ")
filenumber = 1

if os.path.isdir(folderpath):
    
    a = input("looking for a specific format? [y/n] ")
    if(a=='y'):
        f = input("What format are you looking for? ")


    ask = input("Should I apply format? [y/n] ")
    if(ask=='y'):
        format = input("What format Should I apply? (ex - .png) ")
    elif(ask=='n'):
        print("OK, moving on...")
    label = input("Enter the new label ")

    for filename in os.listdir(folderpath):
        name,extension = os.path.splitext(filename)
        if(a=='y' and f==extension):
            if(ask=='y'):
             os.rename(folderpath + '\\' + filename, folderpath + '\\' + label + str(filenumber) + format)
            else:
             os.rename(folderpath + '\\' + filename, folderpath + '\\' + label + str(filenumber) + extension)
        else:
            if(ask=='y'):
             os.rename(folderpath + '\\' + filename, folderpath + '\\' + label + str(filenumber) + format)
            else:
             os.rename(folderpath + '\\' + filename, folderpath + '\\' + label + str(filenumber) + extension)
 

        filenumber +=1
else:
    print("No such Path")



