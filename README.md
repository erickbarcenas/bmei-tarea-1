# [bmei-tarea-1] 


| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | 1 | 
| **TSR-2022-I** | Tarea *01* |
| **Robotica-2022-I**  | Tarea *01* |
| **IT102321-C002** | Sistema Ciber-Físico - Proyecto - Módulo |

## Contenido

- [Objetivo](#objetivo)
- [Introducción](#introduccion)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)

## Objetivo

Hacer que un robot modifique su comportamiento a partir de los siguientes comandos de texto:

- Avanza  [velocidad lineal]

- Gira        [velocidad angular]

- Detente

## Introducción
En el presente programa hace uso de conceptos como nodo, publicador, suscriptor, topic y message. 


**Nodos**: los nodos encapsulan los diferentes procesos que corren en un sistema robótico, por lo general cada nodo debería encargarse de una única tarea [1].

**Topics**: 
Como se podrá suponer, los nodos necesitan comunicarse entre sí para realizar sus tareas. ROS resuelve el problema de la comunicación entre nodos mediante un sistema de publicaciones y suscripciones a topics. Cada topic es un canal de información, donde los nodos pueden escribir o publicar datos, o bien suscribirse para obtener la información que otros nodos publican [1].

**Messages**:
Los mensajes son el equivalente a los tipos de datos en ROS. Cada topic debe definir su nombre y el tipo de mensajes que se van a publicar. Los mensajes se definen por medio de archivos .msg, en estos se indica línea por línea el tipo y nombre de cada variable en el mensaje [1]. 


Ahora bien, 
el funcionamiento del programa es el siguiente:
 1. De manera manual se publica un string.
 2. Se lee el string.
 3. Dependiendo de la cadena de texto (string) ejecuta una rutina.

## Desarrollo

Youtube videos

[![En el siguiente video se documentó el funcionamiento del programa](https://media.discordapp.net/attachments/891388181361082421/904776459015585842/Imagen1.png?width=506&height=499)](https://youtu.be/3t86bYQ5HU0)



##### Ejecución del programa

   Acceda a cd /bmei-tarea-1/src/robot_comm/src
   y en diferentes terminales ejecute las siguientes instrucciones:
1. roscore
2. roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
3. rosrun robot_comm pub_sub.py
4. rostopic pub /recognizer/output std_msgs/String "data: *"
   
   Sustituir el * de la cadena "data: *" como se muentra en los
   siguientes ejemplos:
   1. "data: avanza"
   2. "data: gira"
   3. "data: detente"
  
##### Actualizar cambios del nodo pub_sub.py
   Acceda a cd /bmei-tarea-1
   
   Ejecute
   1. catkin_make
   2. rosrun robot_comm pub_sub.py
   
##### ¿Ha creado un nuevo nodo?
   Acceda a cd /bmei-tarea-1/src/robot_comm/src
   Ejecute
   1. chmod +x node_name.py
      ej. chmod +x pub_sub.py
   2. cd /bmei-tarea-1/
   3. catkin_make
   4. rosrun robot_comm node_name.py
      ej. rosrun robot_comm pub_sub.py
      
## Conclusiones

El robot solo tiene velocidad lineal en el eje x y velocidad angular en el eje z.


## Autor

**Autor** Bárcenas Martínez Erick Iván [GitHub profile](https://github.com/erickbarcenas)


## Referencias

_Referencia simple_

<a id="1">[1]</a>  “ROS - Cerlab Wiki,” Ucr.ac.cr. [En línea]. Disponible en: https://cerlab.ucr.ac.cr/wiki/index.php/ROS. [Recuperado: 01-Nov-2021].


