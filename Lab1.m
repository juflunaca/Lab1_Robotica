%% pyenv("Version",)
rosinit; %Conexion con nodo maestro

%% Ejecutar el codigo (1)
velPub = rospublisher('turtle1/cmd_vel','geometry_msgs/Twist'); %Creación publicador
velMsg = rosmessage(velPub); %Creaci ́on de mensaje

%% Ejecutar el codigo (2)
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)

%% Suscribirse al topico de la simulacion de Turtle1
poseSub = rossubscriber("/turtle1/pose","turtlesim/Pose");
lastmsg = poseSub.LatestMessage;
lastmsg %#ok<NOPTS> 

%% Enviar todos los valores asociados a la pose de Turtle1
posePub = rospublisher('turtle1/cmd_vel','geometry_msgs/Twist');
poseMsg = rosmessage(posePub);
poseMsg.Linear.X = 2;
poseMsg.Linear.Y = 2;
poseMsg.Angular.Z = pi/2;
send(posePub,poseMsg);
pause(1)

%% Finalizar el nodo maestro en MATLAB
rosshutdown;