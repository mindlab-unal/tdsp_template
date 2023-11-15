# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Predicción de precios de combustibles en Colombia

## Objetivo del Proyecto

El objetivo de este proyecto es generar una herramienta que permita predecir a nivel de EDS (Estación de Servicio) el precio de los combustibles cómo el gas natural vehicular y los combustibles líquidos (corriente, extra y diesel).

## Alcance del Proyecto

Para esta primera entrega, se contempla unciamente el uso de los datos correspondientes a gas natural vehicular, sin embargo, se espera incluir también los datos de combustibles líquidos que en estos momentos se encuentran en mantenimiento.

### Datos
Los datos disponibles en esta primera iteración son 11.195 registros al 14 de noviembre de 2023 desde el 1 de enero de 2018. Esta base se va alimentando de manera diaria con los precios reportados por las diferentes EDS. Esta compuesto por 12 columnas asociadas a la fecha del registro, la ubicación del municipio de la EDS, su nombre y el precio publicado. Mayor información sobre este conjunto de datos se puede encontrar en [Link](https://www.datos.gov.co/Minas-y-Energ-a/Consulta-Precios-Promedio-de-Gas-Natural-Comprimid/he3q-86dn)

### Resultados esperados

Se espera obtener un modelo de pronóstico de los precios haciendo uso de técnicas de series temporales de manera que sea posible predecir con cierto nivel de confianza el precio en una EDS dada en un horizonte de tiempo definido.

## Metodología

Se seguirá la metodología CRISP-DM para la exploración y modelamiento del problema, donde se tiene como variable objetivo el precio y será pronosticado utilziando técnicas de series temporales.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 1/2 semanas | del 7 al 17 de noviembre |
| Preprocesamiento, análisis exploratorio | 1/2 semana | del 18 al 21 de noviembre |
| Modelamiento y extracción de características | 1 semana | del 22 al 28 de noviembre |
| Despliegue | 1 semana | del 29 de noviembre al 5 de diciembre |
| Evaluación y entrega final | 1/2 semanas | del 6 de diciembre al 8 de diciembre |

## Equipo del Proyecto

- Desarrollado por **Heiler Santiago Gómez Prieto**
