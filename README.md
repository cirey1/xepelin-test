# xepelin-test
Prueba tecnica Xepelin

# Ejercicios

Script de facil uso, solamente se necesita python 3 instalado y poder correr el siguiente comando `python script_1.py` o `python script_2.py`

## Ejercicio 1
Dentro de este ejercicio, intente reducir la cantidad de evaluaciones (asumiendo que en otros casos, las evaluaciones pueden ser costosas). Entonces hice el minimo de casos (2) para poder ir construyendo un string y posteriormente, cambiar su primera letra a mayuscula (esto facilitaba la reducción de comparaciones)

## Ejercicio 2
En este ejercicio, tome el approach más basico en donde se itera sobre las posiciones dos veces pero, en la segunda iteración, iterando desplazado en una posicion. De esta forma, podemos iterar sobre toda la lista buscando combinaciones de dos numeros que nos entregue el resultado esperado (lo cual deje expresado como parametro para escalarlo). En caso de no encontrarlo, retornamos False. 


# MVP
(URL NO ASEGURADA CON HTTPS DADO QUE NO SE VIO LA NECESIDAD DE SACAR UN CERTIFICADO)

URL: http://3.142.219.141:8000/

## Que se utilizo
Dentro de este MVP, se utilizo Django junto con allauth para poder entregar una sencilla plataforma web que se pudiera observar el html con el embedded del google sheet. Para hacer el embedded del gsheet, se utilizo un `<iframe />` con un source correspondiente al gsheet que se entrego, se habilito la visualización de este para todos pero solamente la edición a quienes tengan permisos (No se puede ver el gsheet, si no ha iniciado sesión).

Posterior a eso, se utilizo `google sheet scripts` para poder realizar un script pequeño que cuando se realiza un cambio en el columna 2 (B), este se ejecuta mandando un POST request hacia la URL entregada y agregando como paramentros el id Operacion (Columna A) y email (Columna C). Tanto el id operación como el email se tomaban de la fila que era editada.

## Razonamiento
Sincronizar Django con Gsheet para hacer push changes, no es tan facíl realizarlo desde django (existe un par de librerias, tales como django-gsheet). Dicho eso, y después de un rato buscando, hizo mucho más sentido gatillar un request desde el mismo google sheet el cual ocupa un lenguage muy parecido a javascript. Dentro de este, habia que filtrar aquellas ediciones de columnas no relevantes (id operacion y email) y al mismo tiempo, habia que obtener los valores de los campos adyacentes a la celda que fue editada. 
