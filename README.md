check docker installation => docker --version

docker information => docker info

List running docker containers  => docker ps
Shows currently running containers.

List all containers => docker ps -a

start an existing containers => docker start django_web_app
It does not create a new container.

stop a containers => docker stop django_web_app

restart a containers => docker restart django_web_app
its equivalent to start and stop 

remove a container => docker rm django_web_app  (-f means force.)

view docker images => docker images or docker image ls 

==================================================================
build a image => docker build . (dot means current directory)
then docker looks for Dockerfile 

build with a custom name => docker build -t my-django-app .  (-t means tag/name the image.)

==================================================================

remove the image => docker rmi my-django-app (If a container is still using that image, Docker may refuse to remove it.)

so force remove image => docker rmi -f my-django-app (-f = force.)

view container logs => docker logs django_web_app

for Django => docker logs django_web_app

for MySQL => docker logs django_mysql

================================================================

Execute a command inside a container => docker exec django_web_app python manage.py check

===============================================================

Docker Compose:

Because our project has multiple services, so instead of managing containers individually we can manage all in one , so that we have to create the 
docker-compose.yml

Start our whole application => docker compose up

start in background => docker compose up -d

Stop the container => docker compose stop (It doesn't remove them)

later we can run => docker compose start

start stopped compose services => docker compose start

stop and remove containers => docker compose down

continue from 26 
 
