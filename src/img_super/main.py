import os
import re
import time
import base64
import logging
import datetime
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import warnings
from typing import Optional

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel('ERROR')

# Set up FastAPI app
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])

# Constants
threshold_low, threshold_high = 0.47, 0.6
MODEL_NAME = 'models/inference_graph'
PATH_TO_SAVED_MODEL = MODEL_NAME + "/saved_model"
LABEL_FILENAME = 'annotations/labelmap.pbtxt'
TAG = []
PATH_TO_SAVED_MODEL_KERAS = 'models/keras/best_model.h5'
name_servicio = "super_puestas"

# Load saved model and build the detection function
def loadModel():
    print('Loading model...', end='')
    start_time = time.time()
    inference_func = tf.saved_model.load(PATH_TO_SAVED_MODEL)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Done! Took {} seconds'.format(elapsed_time))
    return inference_func

def loadModelH5():
    print('Loading model...', end='')
    start_time = time.time()
    inference_func = tf.keras.models.load_model(PATH_TO_SAVED_MODEL_KERAS)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Done! Took {} seconds'.format(elapsed_time))
    return inference_func

detect_fn = loadModel()
detect_keras = loadModelH5()


# Configure logging
LOG_FILENAME = f'log_{name_servicio}.log'
logging.basicConfig(
    filename=LOG_FILENAME, 
    filemode='a', 
    format='%(name)s - %(levelname)s - %(message)s', 
    level=logging.DEBUG)
logger = logging.getLogger("DEBUG")
logging.getLogger("werkzeug").setLevel(logging.ERROR)
# Set global variables
saved_img = False
print_solution = False
save_crop = False
LABEL_FILENAME = 'annotations/labelmap.pbtxt'

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

threshold_low, threshold_high = 0.47, 0.6

class Input(BaseModel):
    image: str
    th_f:Optional[str] = None
    reco_front: Optional[str] = None
    res_front: Optional[dict] = None
    score_front: Optional[float] = None
    threshold_high: Optional[str] = None
    threshold_low: Optional[str] = None
    track_columns: Optional[str] = None

class Output(BaseModel):
    y_min:int
    x_min:int
    y_max:int 
    x_max:int

class OutSuper(BaseModel):
    score:float
    reco:str
    coord:dict

another_strategy = tf.distribute.MirroredStrategy()
another_strategy = tf.distribute.MirroredStrategy()
# Loading the model using lower level API

def loadModel():

    print('Loading model...', end='')
    start_time = time.time()

    # Load saved model and build the detection function
    inference_func = tf.saved_model.load(PATH_TO_SAVED_MODEL)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Done! Took {} seconds'.format(elapsed_time))
    return inference_func

def loadModelH5():

    print('Loading model...', end='')
    start_time = time.time()
    # Load saved model and build the detection function
    inference_func = tf.keras.models.load_model(PATH_TO_SAVED_MODEL_KERAS)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Done! Took {} seconds'.format(elapsed_time))
    return inference_func



def prediction_keras(image_np):
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]
    predecir_t1 = time.time()
    detections = detect_keras.predict(input_tensor)
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
    detections['num_detections'] = num_detections
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    return (detections['detection_boxes'],
            detections['detection_scores'],
            detections['detection_classes'],
            detections['num_detections'])

def prediction(image_np):

    # (boxes, scores, classes, num) = self.sess.run([self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections], feed_dict ={self.image_tensor: image_np_expanded})
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]
    # # Obtener los índices de los tensores de entrada y salida del modelo
    # input_details = interpreter.get_input_details()
    # output_details = interpreter.get_output_details()
    # logger.debug("\n",input_details)
    # logger.debug("\n tamaño tensor",input_tensor.shape)

    # # Establecer los datos de entrada
    # interpreter.set_tensor(input_details[0]['index'], input_tensor)

    # # Realizar la inferencia
    # interpreter.invoke()

    # # Obtener los resultados
    # output_data = interpreter.get_tensor(output_details[0]['index'])


    predecir_t1 = time.time()




    detections = detect_fn(input_tensor)
    # detections = detect_fn.signatures['serving_default'](inputs=input_tensor)

    print(f"113 Tiempo de predicho : {time.time()-predecir_t1}\n")

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
    detections['num_detections'] = num_detections
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    return (detections['detection_boxes'],
            detections['detection_scores'],
            detections['detection_classes'],
            detections['num_detections'])
        # return (boxes, scores, classes, num)

def load_image_into_numpy_array_OpenCV(image):
    return np.array(image).reshape((image.shape[0], image.shape[1],3)).astype(np.uint8)

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
      path: the file path to the image

    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))


def output_front_and_back_OpenCV(image):
    #image = cv2.imread(image_path,1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_np = load_image_into_numpy_array_OpenCV(image)
    image_np_expanded = np.expand_dims(image_np, axis=0)
    return image_np_expanded,image_np

def search_first_entry_and_coords(classes,scores, boxes,class_search):
    """Search first register for coords and class
        - Normaly tf give this information sorted
        - first register always is with the class and score more high

    Args:
        classes (_type_): _description_
        scores (_type_): _description_
        boxes (_type_): _description_
        class_search (_type_): _description_

    Returns:
        _type_: _description_
    """
    index_val = 0
    for i in range(classes.shape[0]):
        if classes[i] == class_search:
            index_val=i
            break
    return scores[index_val],boxes[index_val],classes[index_val]

def read_label_map(label_map_path):
    with open(label_map_path, 'r') as f:
        label_map = f.read()
    label_dict = []
    for match in re.finditer('item\s*{\s*id:\s*(\d+)\s*name:\s*\'([^\']+)\'\s*}', label_map):
        label_name = match.group(2)
        label_dict.append(label_name)
    return label_dict

TAG = read_label_map(LABEL_FILENAME)
detect_fn = loadModel()
detect_keras = loadModelH5()


@app.get("/")
async def root():
    """
    Realiza una prueba de vida del servicio
    
    Retorna un objeto JSON con los siguientes campos:
    
    - **"message"**: "El servicio esta en línea y funcionando correctamente"
    """
    return {"message": "El servicio está en línea y funcionando correctamente"}

@app.post("/super")
async def super(input_data: Input):
    """
    El endpoint /super utiliza un enfoque combinado de dos redes neuronales para detectar y validar si una imagen contiene un rostro superpuesto.

    Primero, se utiliza una red neuronal más rápida (faster) para identificar la ubicación aproximada del rostro en la imagen. Esta red se encarga de realizar una detección rápida pero menos precisa del rostro.

    Una vez que se han obtenido las coordenadas aproximadas del rostro, se recorta esa región de la imagen original y se pasa a través de una red neuronal convolucional (CNN) para realizar una validación más precisa. La CNN está diseñada para determinar si el rostro recortado corresponde a una imagen superpuesta o no.

    El resultado de la predicción se devuelve como un score (puntuación), que indica la probabilidad de que la imagen contenga un rostro superpuesto. Si el score es mayor o igual a 0.5, se considera que la imagen tiene un rostro superpuesto, y se establece el valor de reco como "TRUE". De lo contrario, se considera que la imagen no tiene un rostro superpuesto, y se establece reco como "FALSE".

    Además, el endpoint también devuelve las coordenadas exactas del rostro detectado en la imagen en el campo coord, lo que permite obtener información adicional sobre la ubicación precisa del rostro superpuesto.

    En resumen, el endpoint utiliza una combinación de una red neuronal más rápida y una CNN para detectar y validar rostros superpuestos en una imagen, proporcionando un score de predicción, un indicador de si la imagen contiene un rostro superpuesto y las coordenadas del rostro detectado.

    - **input_data**: Datos de entrada que incluyen la imagen codificada en base64.

    Retorna un objeto JSON con los siguientes campos:
    - "score": Puntuación de la predicción adicional.
    - "reco": Resultado de la predicción adicional ("TRUE" o "FALSE").
    - "coord": {y_min, x_min, y_max, x_max} con los valores individuales de cada coordenada de identificacion.
    """
    name_file_const, name_file = "myImage", "myImage" 
  
    print(f"--------Servicio {name_servicio} INICIO ------")
    print(f"Fecha y Hora de consulta: {datetime.datetime.now()}\n")
    logger.debug("\n")
    logger.debug(f"--------Servicio {name_servicio} INICIO ------")
    logger.debug(f"Fecha y Hora de consulta: {datetime.datetime.now()}\n")

    tiempo_inicial = time.time()
    th = input_data.th_f if input_data.th_f else "-1"
    logger.debug(f"Threshold: {th}")
    
    binary_img = base64.b64decode(input_data.image.replace("data:image/jpeg;base64,", ""))
            
    image = np.asarray(bytearray(binary_img), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    height, width, _ = image.shape

    image_np_expanded, image_np = output_front_and_back_OpenCV(image)
   
    print(f"Tiempo de llegada y cargada de imagenes: {time.time()-tiempo_inicial}")
    coord = await process_image(input_data)
    coord1 = coord.json()
    logger.debug(f"Cooredenadas del rostro en la imagen:{coord1}")
    # # Crea una matriz de coordenadas originales en el formato [y_min, x_min, y_max, x_max]
    print(coord.y_min, coord.x_min, coord.y_max, coord.x_max)
    pad = int((int(coord.x_max)-int(coord.x_min))*0.05)
    crop = image[int(coord.y_min):int(coord.y_max+pad),int(coord.x_min-pad):int(coord.x_max+pad)]
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    
    # Crear la carpeta si no existe
    if not os.path.exists('images_post'):
        os.makedirs('images_post')

    cv2.imwrite("images_post/"+name_file_const+".png", crop)
    # Ejemplo de carga de una imagen y generación de una predicción
    image_path = "images_post/"+name_file_const+".png"
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(640,480))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0  # Normalizar los valores de píxeles entre 0 y 1
    image_array = np.expand_dims(image_array, axis=0)
    prediction = detect_keras.predict(image_array)
    if prediction[0] >= 0.5:
        result = "TRUE"
    else:
        result = "FALSE"

    print("Predicción:",prediction[0],  result)
    logger.debug(f"Tiempo de Total del servicio: {time.time()-tiempo_inicial}")
    logger.debug("correcto termino servicio!!\n\n")
    print(f"Tiempo de Total del servicio: {time.time()-tiempo_inicial}")
    print(f"------------------------TERMINO Servicio {name_servicio}------------------------------------")
    logger.debug(f"-----------------------TERMINO Servicio {name_servicio}------------------------------------")
    return OutSuper(score=prediction, reco=result, coord= coord)



@app.post("/face")
async def process_image(input_data: Input):
    """
    El endpoint /face utiliza un redes neuronal para detectar y validar si una imagen contiene un rostro superpuesto.

    Primero, se utiliza una red neuronal más rápida (faster) para identificar la ubicación aproximada del rostro en la imagen. Esta red se encarga de realizar una detección rápida pero menos precisa del rostro.

    Una vez que se han obtenido las coordenadas aproximadas del rostro retorna las cooredenadas.

    - **input_data**: Datos de entrada que incluyen la imagen codificada en base64.
  
    Retorna un objeto JSON con los siguientes campos:
    - y_min, x_min, y_max, x_max JSON con los valores individuales de cada coordenada de identificacion.

    """
    print(f"--------Servicio {name_servicio} INICIO ------")
    print(f"Fecha y Hora de consulta: {datetime.datetime.now()}\n")
    logger.debug("\n")
    logger.debug(f"--------Servicio {name_servicio} INICIO ------")
    logger.debug(f"Fecha y Hora de consulta: {datetime.datetime.now()}\n")

    tiempo_inicial = time.time()
    th = input_data.th_f if input_data.th_f else "-1"
    logger.debug(f"Threshold: {th}")
    
    binary_img = base64.b64decode(input_data.image.replace("data:image/jpeg;base64,", ""))
            
    image = np.asarray(bytearray(binary_img), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    height, width, _ = image.shape

    image_np_expanded, image_np = output_front_and_back_OpenCV(image)
   
    print(f"Tiempo de llegada y cargada de imagenes: {time.time()-tiempo_inicial}")
    logger.debug(f"Tiempo de llegada y cargada de imagenes: {time.time()-tiempo_inicial}\n")

    predecir_t = time.time()
    (boxes, scores, classes, num) = prediction(image_np)
    print(f"Tiempo de predicho : {time.time()-predecir_t}\n")
    logger.debug(f"Tiempo de predicho: {time.time()-predecir_t}\n")
    final_json = {}
    coor_json = {}
    for i, tag in enumerate(TAG):
        score, box_relative, classImg = search_first_entry_and_coords(classes, scores, boxes, i + 1)
        final_json[tag] = float(score)
        coor_json[tag] = (box_relative)
    boxes = coor_json['F1_F']
    # Multiplica las coordenadas por las dimensiones de la imagen
    y_min = boxes[ 0] * height
    x_min = boxes[ 1] * width
    y_max = boxes[ 2] * height
    x_max = boxes[ 3] * width

    # Crea una matriz de coordenadas originales en el formato [y_min, x_min, y_max, x_max]
    print(y_min, x_min, y_max, x_max)
    output = Output(
        y_min= int(y_min), 
        x_min= int(x_min), 
        y_max= int(y_max), 
        x_max= int(x_max)
    )

    logger.debug(f"Tiempo de Total del servicio: {time.time()-tiempo_inicial}")
    logger.debug("correcto termino servicio!!\n\n")
    print(f"Tiempo de Total del servicio: {time.time()-tiempo_inicial}")
    print(f"------------------------TERMINO Servicio {name_servicio}------------------------------------")
    logger.debug(f"-----------------------TERMINO Servicio {name_servicio}------------------------------------")

    return output


