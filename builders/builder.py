import os as os
import pandas as pd

root = "Productos/"

index_template = open("templates/index.html", "r").read()
index_product_template = open("templates/index_product.html", "r").read()
view_template = open("templates/product_view.html", "r").read()
view_image_template = open("templates/product_view_image.html", "r").read()


def GetImages(image_name):
    all_images = os.listdir(root + image_name)
    all_images.sort()
    return all_images


def RenameImages(image_name):
    """Asumes that path contains the images to rename"""
    path = root + image_name
    for index, image in enumerate(GetImages(image_name)):
        old_name = path + "/" + image
        unused, file_extension = os.path.splitext(old_name)
        new_name = path + "/" + image_name + str(index) + file_extension 
        print("Old:", old_name)
        print("New:", new_name)
        os.rename(old_name, new_name)


def BuildProductViewHtml(image_name, descripcion, fecha):
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



def BuildIndexProduct(nombre, precio, dimensiones):
    first_image_path = GetImages(nombre)[0]
    return "\n" + index_product_template.format(PLACEHOLDER_FOR_NAME=nombre,
        PLACEHOLDER_FOR_IMG=first_image_path,
        PLACEHOLDER_FOR_PRECIO=precio,
        PLACEHOLDER_FOR_DIMENSIONS=dimensiones)


def BuildIndexHtml(placeholder_for_products):
    f = open("index.html", "w")
    f.write(index_template.format(PLACEHOLDER_FOR_PRODUCTS=placeholder_for_products))
    f.close()


def BuildSite():
    df = pd.read_excel(root + "Productos.xlsx")
    products = ""
    for index, row in df.iterrows():
        print("Row:", row)
        nombre = row["Nombre"]
        precio = row["Precio"]
        dimensiones = row["Dimensiones"]
        descripcion = row["Descripcion"]
        fecha = row["Fecha"]
        print(nombre, precio, dimensiones, fecha, descripcion)

        RenameImages(nombre)
        BuildProductViewHtml(nombre, descripcion, fecha)
        products += BuildIndexProduct(nombre, precio, dimensiones)

    BuildIndexHtml(products)


BuildSite()