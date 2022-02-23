from os import listdir
from os.path import isfile, join

f = open("templates/view_template.html", "r")
view_template = f.read()
print(view_template)

def RenameImagesInPath(path="", new_name=""):
    """Asumes that path contains the images to rename"""
    i = 1
    for image in listdir(path):
        os.rename(path + image, path + new_name + i + ".png")
        i += 1

for creacion in listdir("creaciones/"):
    print(creacion)

    f = open("creaciones/" + creacion + ".html", "w")
    f.write(view_template)
    f.close()
