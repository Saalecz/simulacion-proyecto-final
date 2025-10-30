# Teoría: Interacción de Imán-Anillo considerando únicamente efectos radiales (Subestimación del efecto)

## **Objetivo específico:**
Desarrollar un modelo discreto simplificado que describa la interacción entre el campo magnético de un imán y las corrientes de Foucault inducidas en cada anillo. Se simplifica tomando únicamente la componente radial de la fuerza de frenado. El objetivo incluye formular las ecuaciones dinámicas y proponer una estrategia computacional para simular la dinámica. 

Inicialmente, partimos de estudiar el caso más simple, en donde se tiene un único anillo *(de grosor despreciable)*, y en su centro se encuentra un imán *(puntual de geometría despreciable)*, el anillo se encuentra en el eje Z de tal manera que el imán cae verticalmente por este eje, inicialmente el anillo tendrá un radio fijo a y su area es $A= \Pi a^{2}$ 

## Interacción Imán-Anillo: 

<img width="300" height="300" alt="imagen" src="https://github.com/user-attachments/assets/3c3d2719-ff24-4a13-8b0b-f7b395d4683f" />

En este sistema, la interacción depende tanto de las propiedades de los materiales involucrados como de la configuración geométrica.

Cuando un imán se aproxima a un anillo conductor, la variación temporal del flujo magnético que atraviesa la superficie del anillo induce corrientes de Foucault _(eddy currents)_ en su interior. Estas corrientes generan campos magnéticos propios que, de acuerdo con la ley de Lenz, se oponen al cambio de flujo que las originó. En consecuencia, pueden producir fuerzas de atracción o repulsión dependiendo de la dirección del movimiento y de la orientación del campo del imán.

En el caso considerado, el imán cae a lo largo del eje de un anillo conductor. El anillo, al ser eléctricamente cerrado, responde a la variación del campo magnético $B(r,t)$ generado por el imán _(cuyo eje principal coincide con el eje del anillo)_, induciendo una corriente azimutal.
**Dado que la magnitud del campo que atraviesa el área del anillo cambia con la distancia entre el imán y el plano del conductor, el flujo magnético varía en el tiempo; esta variación es la responsable de la generación de las corrientes inducidas.**

_(Esta geometría cerrada del anillo podría evaluarse experimentalmente en etapas posteriores para analizar la dependencia del fenómeno con la conductividad del material y la distancia entre elementos.)_

La interacción descrita constituye un fenómeno de inducción electromagnética, mediante el cual un campo magnético variable induce corrientes eléctricas en un material conductor. Este proceso se describe con la ley de Faraday-Lenz, que establece que toda variación del flujo magnético a través de una superficie genera una corriente inducida que se opone al cambio que la produjo:

$$\phi(t)= \int_{s} B(r,t).dS$$

Para estudiar este sistema existen dos aproximaciones posibles:
* Partir del imán como un dipolo magnético
* Estudiar el sistema con un imán real

Adoptando inicialmente la primera aproximación, el momento magnético del dipolo $m=m\hat{z}$ hace referencia a la intensidad y dirección del campo. Este campo que genera el imán es axialmente simétrico, es decir, tendrá la misma forma en todos los puntos equidistantes al eje $z$ y disminuye rápidamente con la distancia, de modo que al alejarse del imán su acción se debilita.

Matemáticamente, el campo magnético que genera un dipolo $m$ en un punto del espacio **r** es:

$$B(r)= \frac{\mu_{0}}{4 \pi r^{3} } [3(m.\hat{r})\hat{r}-m]$$

y, sobre el eje axial, teniendo en cuenta que $(m.\hat{r})= m(\hat{z}.\hat{z})=m$ y $3(m.\hat{r}) - m= 3m(\hat{z}) - m\hat{z}=2m\hat{z}$, se reduce a:


$$B_{z}(z)= \frac{\mu_0}{2 \pi} \frac{m}{z^{3}}$$, lo que se conoce como campo dipolar axial, y será nuestra primera aproximación para modelar el sistema en su caso mas simple. 

Ahora, ¿qué pasa cuando el imán no es puntual o el anillo tiene grosor no despreciable? 
