import os as os
import pandas as pd

root = "Productos/"

f = open("templates/index_template.html", "r")
index_template = f.read()

f = open("templates/index_product_template.html", "r")
index_product_template = f.read()

f = open("templates/view_template.html", "r")
view_template = f.read()

f = open("templates/view_image_template.html", "r")
view_image_template = f.read()


def GetImages(image_name):
    all_images = os.listdir(root + image_name)
    all_images.sort()
    return all_images


def RenameImages(image_name, new_name_base):
    """Asumes that path contains the images to rename"""
    path = root + image_name
    for index, image in enumerate(GetImages(image_name)):
        old_name = path + "/" + image
        unused, file_extension = os.path.splitext(old_name)
        new_name = path + "/" + new_name_base + str(index) + file_extension 
        print("Old:", old_name)
        print("New:", new_name)
        os.rename(old_name, new_name)


def BuildViewHtml(image_name, descripcion, fecha):
    all_views = ""
    for index, image in enumerate(GetImages(image_name)):
        full_name = image_name + "/" + image
        all_views += ("\n" + view_image_template.format(PLACEHOLDER_FOR_FULL_NAME=full_name)) 

    view = view_template.format(PLACEHOLDER_FOR_TITLE=image_name,
        PLACEHOLDER_FOR_DESCRIPTION=descripcion,
        PLACEHOLDER_FOR_BRICKS=all_views,
        PLACEHOLDER_FOR_DATE=fecha)
    f = open(root + image_name + ".html", "w")
    f.write(view)
    f.close()



def GenerateIndexProduct(nombre, image_name, precio, dimensiones):
    return "\n" + index_product_template.format(PLACEHOLDER_FOR_NAME=nombre,
        PLACEHOLDER_FOR_IMG=image_name,
        PLACEHOLDER_FOR_PRECIO=precio,
        PLACEHOLDER_FOR_DIMENSIONS=dimensiones)


def BuildIndexHtml(placeholder_for_products):
    f = open("index.html", "w")
    f.write(index_template.format(PLACEHOLDER_FOR_PRODUCTS=placeholder_for_products))
    f.close()


def BuildSite():
    df = pd.read_excel(root + "Productos.xlsx")
    placeholder_for_products = ""
    for index, row in df.iterrows():
        print("Row:", row)
        nombre = row["Nombre"]
        precio = row["Precio"]
        dimensiones = row["Dimensiones"]
        descripcion = row["Descripcion"]
        fecha = row["Fecha"]
        print(nombre, precio, dimensiones, fecha, descripcion)

        # Task 1
        print("Task 1")
        RenameImages(nombre, nombre)

        # Task 2
        print("Task 2")
        BuildViewHtml(nombre, descripcion, fecha)

        # Task 3
        print("Task 3")
        image_name = GetImages(nombre)[0]
        placeholder_for_products += GenerateIndexProduct(nombre, image_name, precio, dimensiones)

    BuildIndexHtml(placeholder_for_products)


BuildSite()