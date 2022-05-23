# **Project Charter**

## **Conocimiento del Negocio**

### **¿Quien es el cliente, y cual es el dominio del cliente en el negocio?**

El cliente es la Junta de Regentes del Sistema de la Universidad de Wisconsin en nombre de UW-Madison y Kaggle.

La Junta de Regentes del Sistema de la Universidad de Wisnonsin consiste de 18 miembros 16 de los cuales son nombrados por el gobierno; La Junta es responsable de establecer políticas y reglas para gobernar el Sistema, planificar para satisfacer las necesidades estatales futuras de educación universitaria, establecer estándares y políticas de admisión, revisar y aprobar los presupuestos universitarios y establecer el marco regulatorio dentro del cual se permite operar a las unidades individuales. con el mayor grado de autonomía posible.

Kaggle es una subsidiaria de Google LLC, es una comunidad en línea de científicos de datos y profesionales del aprendizaje automático. Kaggle permite a los usuarios buscar y publicar conjuntos de datos, explorar y crear modelos en un entorno de ciencia de datos basado en la web. Esta plataforma permite realizar challenges sobre aprendizaje automático y profundo, realizados por particulares, he de aquí donde hemos tomado como proyecto este desafío.

### **¿Cuál es problema del negocio que se desea resolver?**

En 2019, aproximadamente 5 millones de personas fueron diagnosticadas con cáncer del tracto gastrointestinal en todo el mundo. De estos pacientes, aproximadamente la mitad son elegibles para la radioterapia, que generalmente se administra durante 10 a 15 minutos al día durante 1 a 6 semanas. Los oncólogos radioterápicos intentan administrar altas dosis de radiación utilizando haces de rayos X que apuntan a los tumores y evitan el estómago y los intestinos. Con tecnología más nueva, como imágenes de resonancia magnética integrada y sistemas de acelerador lineal, también conocidos como MR-Linacs, los oncólogos pueden visualizar la posición diaria del tumor y los intestinos, que puede variar día a día. En estas exploraciones, los oncólogos radiólogos deben delinear manualmente la posición del estómago y los intestinos para ajustar la dirección de los haces de rayos X para aumentar la administración de la dosis al tumor y evitar el estómago y los intestinos. Este es un proceso que requiere mucho tiempo y mano de obra que puede prolongar los tratamientos de 15 minutos a una hora por día, lo que puede ser difícil de tolerar para los pacientes, a menos que el aprendizaje profundo pueda ayudar a automatizar el proceso de segmentación. Un método para segmentar el estómago y los intestinos haría que los tratamientos fueran mucho más rápidos y permitiría que más pacientes recibieran un tratamiento más efectivo.

## **Alcance**
### **¿Cuál solución de ciencia de datos se desea realizar?**
  
Para este problema se desea realizar un modelo de aprendizaje profundo para segmentar los órganos vitales en las imágenes de resonancias magnéticas de los pacientes.

### **¿Como se hará?**

Para esto se creará un pipeline que procese las imágenes ajustándolas según nuestro análisis y se entregue estas imágenes analizadas a un modelo de aprendizaje profundo que nos arroje la imagen con la demarcación de los órganos vitales y su grado de confiabilidad en su interpretación.

### **¿Como va a ser consumido esto por el cliente?**

La idea será construir un servicio web que reciba la imagen y esta sea entregada al pipeline para ser analizada y posteriormente ser devuelta con su resultado final.

## **Personal**
* El equipo está conformado por:

  * Líder de proyecto
  * Científico de datos
  * Desarrollador de Software
## **Métricas**
* Aumentar la precisión de detección de órganos vitales en las resonancias magnéticas aplicadas a los pacientes diagnosticados con cáncer gastrointestinal.
* Disminuir el tiempo de las secciones de radiología de una hora a 15 minutos aproximadamente en un numero alto de secciones de radiología.
* Alcanzar un alto nivel de precisión en la detección de órganos vitales en las resonancias magnéticas a un 80% de confiabilidad.
* Actualmente los médicos o oncólogos se demoran por sección más 15 minutos hasta una hora analizando las resonancias magnéticas para poder detectar órganos vitales y así aplicar altas dosis a los tumores.
* Para poder determinar el éxito del modelo debemos tener unas métricas de confiabilidad mayores o iguales al 80% de las imágenes procesadas, de esta forma estaremos bajando los tiempos de tratamiento considerablemente.

## Plan
* Las fases a ejecutar son las siguientes:
  
  * **Consolidación del equipo y selección del proyecto**: En esta etapa se formara el equipo, se creara las politicas de trabajo y se escogera el proyecto a ejecutar.
  
  * **Análisis de la información**: En esta etapa se comenzara con el análisis de la inforamción y la definición del proyecto y sus entregables.
  
  * **Elaboración del Pipeline de pre-procesamiento**: Se comenzara con la elaboración del Pipeline que se ejecutara para que las imagenes sea procesada para cada paciente.
  
  * **Elaboración del Modelo de Aprendizaje Profundo**: Esta etapa se construye el primer modelo y se hara una depuración ciclica del mismo hasta optener el mejor resultado.
  
  * **Creación del Servicio web con Node JS**: Se procedera a crear un web services para recopilar la data y devolver la el analisis de esta misma.
  
  * **Puesta en producción de la solución**: Creación de los servidores o servición en la nube de AWS para la solución.


![Cronograma](./cronograma.png?raw=true)

## Arquitectura
* Datos
  * Se provee un grupo de datos del cliente en el cual contiene la información de imágenes por sección de un grupo de pacientes con la información de la ubicación de cada órgano en las imágenes.

* Que herramientas y recursos se van a utilizar en la solución
  * Se usará Python para construcción, segmentación y muestreo de características de cada imagen.
  
  * TensorFlow para la construcción del modelo de aprendizaje profundo.
  
  * Node JS, para la construcción de un servidor en el cual se despliegue el servicio web y poder enviar las imágenes de los pacientes y poder hacer la segmentación.
  
* Diagramas para entendimiento de la solución
  * Diagrama de infraestructura

  ![diagrama de infraestructura](./diagrama_infraestructura.png?raw=true)<br/>

  * Imágenes que se van a recibir y ejemplos esperados de salida proveídos por el modelo.
  
  <br/>
  
  ![Imagen de Entrada e imagen de salida](./data_in_data_out.png?raw=true)
  <center>Imagen 1 de resonancia magnética que después de ser procesada debería retorna resaltado con máscaras en la misma imagen las posición del intestino delgado, grueso y estómago.</</center>

  <br/>

  ![Imagen 2 de Entrada e imagen 2 de salida](./data_in_data_out_2.png?raw=true)
  <center>Imagen 2 de resonancia magnética que después de ser procesada debería retorna resaltado con máscaras en la misma imagen las posición del intestino delgado, grueso y estómago.</</center>

  <br/>

  ![Imagen 3 de Entrada e imagen 3 de salida](./data_in_data_out_3.png?raw=true)
  <center>Imagen 3 de resonancia magnética que después de ser procesada debería retorna resaltado con máscaras en la misma imagen las posición del intestino delgado, grueso y estómago.</</center>

  <br/>


## **Comunicación**
* Se creo un grupo en WhatsApp como herramienta de comunicación, la cual diariamente el equipo está informando sobre avances realizados, en que se estará enfocando y si tiene alguna duda al respecto sobre su tarea actual.
* En proyecto al ser una competencia en Kaggle nuestro contacto será el líder del equipo en Kaggle quien es: **Camilo Zambrano**
