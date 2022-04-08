# Lab1_Robotica
## Por: Julian Luna y Javier Caicedo

### *a. Familiarizarce con Los comandos de Linux*

1. pwd: "Print Working Directory", imprime en la terminal el directorio en que estamos ubicados.
2. ls: Muestra todos los subdirectorios y archivos que se encuentran en el directorio actual. 
3. cd: Permite movernos entre directorios, dependiendo de los argumentos entregados.
4. touch: Crea un nuevo archivo segun la especificacion que le demos.
5. rm: Borra un archivo especificado.
6. mkdir: Crea un nuevo subdirectorio en el directorio actual.
7. rmdir: Borra un directorio especificado; esto es porque los directorios no puden ser borrados con el comando "rm".
8. mv: Usado para mover un archivo de un directorio a otro y tambien para cambiar los nombres de archivos. Puede ser usado para ambas cosas al tiempo.
9. cp: Funciona de forma similar al comando "mv", pero creando una copia del archivo en vez de moviendo el original.
10. man: Abre el manual de un comando especificado, permite ver que argumentos pueden ser adicionados para realizar acciones diferentes o complementarias.

### *b. Conexión de ROS con MATLAB*

Empezaremos iniciando 2 terminales, en la primera lanzaremos el nodos maestro con el comando roscore y en la segunda colocaremos el comando rosrun turtlesim turtlesim_node para inicializar un nodo del paquete.

En la primera terminal colocamos el comando roscore.
<p align="center"><img src="https://i.postimg.cc/W3xLyX44/1a.png" width="450"></p>
En la segunda terminal colocamos el comando rosrun turtlesim turtlesim_node.
<p align="center"><img src="https://i.postimg.cc/vHFwLqjq/2.png" width="450"></p>

Vemos como emerge una tortuga en un canvas de fondo azul.
<p align="center"><img src="https://i.postimg.cc/bvNhSZMq/3.png" width="360"></p>
Posteriormente desde Matlab, lanzaremos una instancia para linux, a través de la ejecución de las siguiente sentencias.
<p align="center"><img src="https://i.postimg.cc/pVntjb05/4.png" width="480"></p>
Al ejecutar las sentencias anteriores realizamos la conexión con el nodo maestro de ROS, creamos un publicador y un objeto de mensaje vinculado a dicho publicados, a través del objeto mensaje, podemos manipular los atributos posicionales de la tortuga, en este caso la posición en X, a la que le atribuiremos el valor de 1,con esto conseguiremos que la tortuga, en este caso, se desplace horizontalmente, esta orden será enviada por medio del comando send, pasando como parámetros el publicador y el objeto de mensaje.

<p align="center"><img src="https://i.postimg.cc/638xzDtS/5.png" width="280"></p>
Ahora crearemos una subsección en nuestro script que nos permita suscribirnos al tópico pose de la simulación de turtle1.
<p align="center"><img src="https://i.postimg.cc/8CKVR1QM/6.png" width="450"></p>
Luego crearemos otra sección que nos permita enviar los valores de los parámetros asociados a pose vinculados al objeto turtle1.

<p align="center"><img src="https://i.postimg.cc/qqnVHytx/7.png" width="450"></p>
La siguiente sentencia nos permitirá detener la ejecución del nodo maestro de ROS desde Matlab.

<p align="center"><img src="https://i.postimg.cc/x1PQdv6s/8.png" width="450"></p>

### *c. Manejo de ROS usando Python*

Empezaremos creando el Script myTeleopKey.py dentro del paquete Hello_turtle, para ello podemos desde Visual Studio Code (VSC) abrir la carpeta en nuestro espacio de trabajo donde se encuentra nuestro paquete Hello_turtle y en el interior de esta abriremos la carpeta Scripts, allí guardaremos nuestro archivo.

Ahora en nuestro Script, importaremos las librerías que nos permitirán manipular el influjo de eventos de entrada, por ejemplo, el modulo termios, la librería cliente para ROS, rospy, así como aquellas vinculadas a servicios que nos permitirán manipular la posición de la tortuga, ofrecidos en el paquete Hello turtle, por ejemplo, los módulos TeleportAbsolute, TeleportRelative y Twist.

<p align="center"><img src="https://i.postimg.cc/rF1XhG28/9.png" width="450"></p>
Luego, escribiremos una función que nos permita obtener el valor de los eventos de entrada, asociados al hecho de oprimir alguna tecla.
<p align="center"><img src="https://i.postimg.cc/cHp2hCDg/10.png" width="450"></p>
Ahora definiremos las funciones que nos permiten hacer el vínculo con los servicios asociados al objeto turtle1 y modificar los atributos de posición.
<p align="center"><img src="https://i.postimg.cc/Mpzkgcz1/11.png" width="450"></p>
Luego definimos la función que le atribuye a cada evento del teclado de nuestro interés el conjunto de acciones que permiten modificar la posición del objeto turtle1.
 
<p align="center"><img src="https://i.postimg.cc/qvQfrk7S/12.png" width="450"></p>

<p align="center"><img src="https://i.postimg.cc/43FrKBV1/13.png" width="450"></p>
Finalmente definimos el main.
<p align="center"><img src="https://i.postimg.cc/5tthNZY0/14.png" width="320"></p>
Ahora incluiremos nuestro Script myTeleopKey.py en el apartado de catkin_install_python del archivo Cmakelist.txt.
<p align="center"><img src="https://i.postimg.cc/4d7jpV1R/15.png" width="320"></p>

<p align="center"><img src="https://i.postimg.cc/7Pzp616g/16.png" width="450"></p>
Luego, en una nueva terminal iremos al directorio del workspace de catkiny ejecutaremos el comando catkin_make para reconstruir el paquete modificado.
<p align="center"><img src="https://i.postimg.cc/4ypMSGM8/17.png" width="450"></p>
Posteriormente en usaremos tres terminales, en la primera reiniciaremos el nodo maestro de ROS con el comando roscore, en la segunda escribiremos el comando rosrun turtlesim turtlesim_node y en la tercera escribiremos el comando source devel/setup.bash y luego el comando rosrun hello turtle myTeleopKey.py y probamos el funcionamiento del script desarrollado.
1ra terminal:
<p align="center"><img src="https://i.postimg.cc/3x86nPZB/18.png" width="450"></p>

<p align="center"><img src="https://i.postimg.cc/pXY4Q2Kr/19.png" width="450"></p>
 2da terminal:
<p align="center"><img src="https://i.postimg.cc/gkP16wX1/20.png" width="450"></p>
 3ra terminal:
<p align="center"><img src="https://i.postimg.cc/zGxQM0t1/21.png" width="450"></p>

<p align="center"><img src="https://i.postimg.cc/HLjNCXR8/22.png" width="320"></p>

<p align="center"><img src="https://i.postimg.cc/9fSnXzH8/23.png" width="360"></p>

### Conclusiones
* La elección apropiada de la librería así como la forma de manipular sus objetos es importante a la hora de trabajar con eventos del teclado en Python, esto porque algunas librerías no tienen un buen rendimiento en Lynux y porque algunas clases de los módulos de control del teclado, detienen la ejecución normal del programa por esperar el evento de entrada del teclado.
* Es importante reconocer los diferentes servicios asociados a los nodos que interactúan en ROS, esto con la intención de conocer los métodos necesarios para el envío y adquisición de información entre ellos y lograr con ello la gestación de estrategias de control personalizadas, como la implementada en este laboratorio.