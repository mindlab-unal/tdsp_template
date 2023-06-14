import os
import cv2
import argparse
from lxml import etree
import xml.etree.ElementTree as ET
from tqdm import tqdm
import subprocess


def generateDict(input_path):
    dict_imgs = dict()
    for file_i in os.listdir(input_path):
        if '.ini' in file_i:
            continue
        if 'DS_Store' in file_i:
            continue
        if '.xml' not in file_i:
            img_lst_i = file_i.split('.')
            if len(img_lst_i) == 2:
                name_img_i,formato_img_i = img_lst_i[0], img_lst_i[1]
            else:
                name_img_i, formato_img_i = ".".join(img_lst_i[:len(img_lst_i)-1]), img_lst_i[len(img_lst_i)-1]
            dict_imgs[name_img_i]=formato_img_i
    return dict_imgs

def get_region_coordinates(xml_path):
    """
    Función que lee un archivo XML y devuelve las coordenadas de la región de interés.
    """
    # with open(xml_path) as f:
    #     xml = f.read()
    # root = etree.fromstring(xml)
    # xmin = int(root.xpath("//xmin/text()")[0])
    # ymin = int(root.xpath("//ymin/text()")[0])
    # xmax = int(root.xpath("//xmax/text()")[0])
    # ymax = int(root.xpath("//ymax/text()")[0])
    # return xmin, ymin, xmax, ymax

        
    # Parseamos el archivo xml para obtener las coordenadas de recorte
    tree = ET.parse(xml_path)
    root = tree.getroot()
    xmin = int(root.find("./object/bndbox/xmin").text)
    ymin = int(root.find("./object/bndbox/ymin").text)
    xmax = int(root.find("./object/bndbox/xmax").text)
    ymax = int(root.find("./object/bndbox/ymax").text)
    print(xmin, ymin, xmax, ymax)
    return xmin, ymin, xmax, ymax

def main(args):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    print(directorio_actual)
    # try:
    #     print(args.dir)
    #     resultado = subprocess.check_output(["python", os.path.join(directorio_actual,"solutionCorrupted_imgs.py"), "-i",args.dir], stderr=subprocess.STDOUT)
    #     print(resultado.decode())
    # except subprocess.CalledProcessError as e:
    #     print(f"Error: {e.output.decode()}")
    # except Exception as e:
    #     print(f"Error: {str(e)}")
    # input('espera ...')
    # Crea la carpeta cut si no existe
    os.makedirs(os.path.join(args.dir,"cut"), exist_ok=True)
    input_path = os.path.join(os.getcwd(), args.dir)
    # os.makedirs(os.path.join(args.dir,"cut"), exist_ok=True)
    dict_imgs=generateDict(input_path)

    for name_i, formato_img_i in tqdm(dict_imgs.items(), total=len(dict_imgs)):
        if name_i != '':

    
    # # Lee todos los archivos XML en la carpeta especificada
    # xml_files = [f for f in os.listdir(args.dir) if f.endswith(".xml")]
    
    # for xml_file in xml_files:
        # Obtiene la ruta de la imagen correspondiente
            image_path = os.path.join(args.dir, name_i+'.'+formato_img_i)
            print(image_path)
            
            # Lee la imagen con OpenCV
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: could not load image {image_path}")
                input('espera 85')
                continue
            print(image.shape)
            if name_i=='10681486':
                print('es ele error')
            # Obtiene las coordenadas de la región de interés
            print(os.path.join(args.dir, name_i))
            if not os.path.isfile(os.path.join(args.dir, name_i +".xml")):
                continue
            xmin, ymin, xmax, ymax = get_region_coordinates(os.path.join(args.dir, name_i +".xml"))
            print(xmin, ymin, xmax, ymax)
            # input('espera')
            # Recorta la imagen y guarda la imagen recortada en la carpeta cut
            try:
                if xmax-10 < image.shape[0] and   ymax-10 < image.shape[1]: 
                    cut_image = image[ymin-10:ymax+10, xmin-15:xmax+15]
                else:
                    cut_image = image[ymin:ymax, xmin:xmax]
                cv2.imwrite(os.path.join(args.dir, "cut", name_i + "."+ formato_img_i), cut_image)
            except:
                cut_image = image[ymin:ymax, xmin:xmax]
                cv2.imwrite(os.path.join(args.dir, "cut", name_i + "."+ formato_img_i), cut_image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recorta imágenes en función de los archivos XML.')
    parser.add_argument('-dir', type=str, help='Ruta de la carpeta que contiene los archivos XML e imágenes.')
    args = parser.parse_args()
    main(args)