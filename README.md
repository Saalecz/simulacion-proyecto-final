# Estudio de la criticalidad y las propiedades emergentes en el frenado magnético de un imán a través de un modelo discreto
## Laboratorio Avanzado III 
### Participantes 
* Sara Alejandra Carvajal Ramírez
* Marlon Jhassir García Velasquez
* Miguel Angel Revelo
* Juan Sebastian Agudelo

## Resumen: 
Este informe presenta una propuesta de investigación sobre un modelo discreto del frenado magnético de un imán en movimiento sobre un medio conductor. El objetivo es comprender cómo las interacciones locales de las corrientes de Foucault generan propiedades macroscópicas emergentes, como la fuerza de frenado y la velocidad terminal. El conductor se modela como un conjunto de anillos acoplados, simulados numéricamente en Python desde una versión 1D hasta una 2D. Se busca identificar puntos críticos y  relaciones de escala que conectan la dinámica microscópica con el comportamiento macroscópico del sistema, aportando una perspectiva complementaria a los modelos continuos tradicionales.

## Objetivo general 
Proponer un modelo discreto que represente el conductor como un conjunto de anillos interactuantes, con el fin de estudiar cómo las corrientes de Foucault locales dan lugar a propiedades macroscópicas de frenado electromagnético, identificando puntos críticos y relaciones de escalamiento con parámetros fundamentales del sistema.

## Objetivos específicos
* **Desarrollar un modelo discreto unidimensional (1D) para el caso anillo-imán:** Describir  las ecuaciones que gobiernan la interacción entre el campo magnético y la corriente inducida en el anillo tomando la fuerza de frenado únicamente radial (subestimación del efecto) y desarrollar computacionalmente el modelo.
* **Analizar la dinámica del sistema 1D:**  haciendo uso de simulaciones numéricas, identificar las condiciones en las que el sistema alcanza el régimen estacionario y caracterizar la fuerza de frenado en función de la velocidad del imán y las propiedades del conductor.
* **Desarrollar el modelo en el caso bidimensional (2D):** Incorporar la interacción entre múltiples anillos y el efecto que genera el imán sobre los otros anillos, de modo que se incluyan los acoplamientos magnéticos entre anillos y entre cada anillo y el imán.
* **Estudiar el comportamiento colectivo del sistema 2D:** evaluar las interacciones locales entre anillos influyen en la evolución temporal de las corrientes inducidas y en la respuesta global del sistema.
* **Caracterizar las propiedades macroscópicas emergentes:** Analizar la fuerza de frenado y la velocidad terminal del imán, estableciendo su relación con las propiedades del material (conductividad eléctrica, geometría del conductor, entre otros) para comprender cómo los parámetros microscópicos del modelo determinan el comportamiento global del sistema.



