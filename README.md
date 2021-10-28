# Tarea 1


## Descripción
Programa que de manera manual se publica un string,
luego se lee y dependiendo de la cadena de texto ejecuta 
una rutina.

## Desarrollo

### Ejecución del programa

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
  
### Actualizar cambios del nodo pub_sub.py
   Acceda a cd /bmei-tarea-1
   
   Ejecute
   1. catkin_make
   2. rosrun robot_comm pub_sub.py
   
### ¿Ha creado un nuevo nodo?
   Acceda a cd /bmei-tarea-1/src/robot_comm/src
   Ejecute
   1. chmod +x node_name.py
      ej. chmod +x pub_sub.py
   2. cd /bmei-tarea-1/
   3. catkin_make
   4. rosrun robot_comm node_name.py
      ej. rosrun robot_comm pub_sub.py
   
## Video de la demostración de la funcionalidad
  https://youtu.be/3t86bYQ5HU0 

## Conclusiones

El robot solo tiene velocidad lineal en el eje x y velocidad angular en el eje z.




