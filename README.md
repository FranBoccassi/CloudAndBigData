# CloudAndBigData

___
___

## Introducción

StackOverflow Questions & Answers es un proyecto que trata de analizar la eficiencia del servidor más popular entre los programadores, el cual tiene muy buena fama.

Este analisis trata de demostrar hasta qué punto es verídico que es uno de los servidores con mejor rendimiento a escala mundial.

### Descripción del problema

A menudo nos encontramos con dudas sobre cómo realizar cierto código en programación, tendemos a pensar que para qué vamos a "reinventar la rueda" pues muchas de las cosas que necesitamos hacer cuando desarrollamos un proyecto de programación, se basa en reutilizar partes de código con diferentes funciones, estas suelen ser el sujeto de nuestras dudas, cómo lo habrán hecho los que ya lo han hecho, cómo será la forma más eficiente... A todo esto en la mayoría de las ocasiones encontramos respaldo en StackOverflow.

### Necesidad del Big Data

Alcanzar a ver todas y cada una de las preguntas junto con sus respectivas respuestas, alcanza un tamaño excesivamente grande, debido a que reune una comunidad a escala mundial. Además, sirve de respaldo para todo tipo de lenguajes de programación. Por este motivo, hemos realizado scripts que facilitan la recopilación de datos y además generan diferentes contrastes de la información, para ello utilizamos una instancia de máquina virtual de Google Cloud con 4vCPU y 3.6Gb de memoria.

### Solución

La solución desarrollada hemos obtenido los dataset's más actualizados, sobre estos realizamos los siguientes procesos: filtrar, analizar, guardar y representar la información obtenida; según los diferentes aspectos que hemos tenido en cuenta como son: el tiempo medio de respuesta, los tags más frecuentes, es decir, lenguajes más usados y aquellos tags que no han obtenido una solución concreta.

Lo que nos ayuda en primer lugar por ejemplo a clarificar la evidencia de la cantidad de preguntas sin solucionar.

Aquí dejamos el enlace para los datasets que hemos utilizado, son demasiado amplios como para subirlos a GitHub:

https://www.kaggle.com/stackoverflow/stacksample


