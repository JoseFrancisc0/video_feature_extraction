# video_feature_extraction

Este repositorio incluye el procedimiento con el cual se extrajeron los feature vectors de cada uno de los videos del training dataset.
Este proceso se apoyó de la librería de [video_features](https://v-iashin.github.io/video_features/models/r21d/) con el modelo de R(2+1)D.

El dataset se sacó a través de una carpeta compartida de Google Drive. 

Para usar este proyecto, se necesita las siguientes instalaciones:

```
! git clone https://github.com/v-iashin/video_features.git
! pip install omegaconf av==10.0
```

También debe contar con un equipo con GPU CUDA para agilizar el proceso de extracción.
En total, el tiempo de extracción de features fue de aproximadamente 7 horas.
El resultado es un csv con los feature vectors del dataset.
