# Teoría: Interacción de Imán-Anillo considerando únicamente efectos radiales (Subestimación del efecto)

## **Objetivo específico:**
Desarrollar un modelo discreto simplificado que describa la interacción entre el campo magnético de un imán y las corrientes de Foucault inducidas en cada anillo. Se simplifica tomando únicamente la componente radial de la fuerza de frenado. El objetivo incluye formular las ecuaciones dinámicas y proponer una estrategia computacional para simular la dinámica. 

Inicialmente, partimos de estudiar el caso más simple, en donde se tiene un único anillo *(de grosor despreciable)*, y en su centro se encuentra un imán *(puntual de geometría despreciable)*, el anillo se encuentra en el eje Z de tal manera que el imán cae verticalmente por este eje, inicialmente el anillo tendrá un radio fijo a y su area es $A= \Pi a^{2}$ 

## Interacción Imán-Anillo: 

<img width="300" height="300" alt="imagen" src="https://github.com/user-attachments/assets/3c3d2719-ff24-4a13-8b0b-f7b395d4683f" />

En este sistema, la interacción depende tanto de las propiedades de los materiales involucrados como de la configuración geométrica.

Cuando un imán se aproxima a un anillo conductor, la variación temporal del flujo magnético que atraviesa la superficie del anillo induce corrientes de Foucault *(eddy currents)* en su interior. Estas corrientes generan campos magnéticos propios que, de acuerdo con la ley de Lenz, se oponen al cambio de flujo que las originó. En consecuencia, pueden producir fuerzas de atracción o repulsión dependiendo de la dirección del movimiento y de la orientación del campo del imán.

En el caso considerado, el imán cae a través del eje de un anillo conductor. El anillo, al ser eléctricamente cerrado, responde a la variación del campo magnético $B(r,t)$ generado por el imán *(cuyo eje principal coincide con el eje del anillo)* induciendo una corriente azimutal. 
**Dado que la magnitud del campo que atraviesa el área del anillo cambia con la distancia entre el imán y el plano del conductor, el flujo magnético varía en el tiempo, y esta variación es la responsable de la generación de las corrientes inducidas.**

_(Esta geometría cerrada del anillo podría evaluarse experimentalmente en etapas posteriores para analizar la dependencia del fenómeno con la conductividad del material y la distancia entre elementos.)_

El flujo magnético a través del anillo se describe a través de la ley de Faraday como: 

$\phi(t)= \int_{s} B(**r**,t).dS$

Ahora, considerando al imán como un dipolo magnético orientado a lo largo del eje z, donde el momento magnético $m=m\hat{z}$
