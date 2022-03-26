# RabbitMQ Hello World with PHP
[Reference](https://www.rabbitmq.com/tutorials/tutorial-one-php.html)

## Environments setup
[Readme.md](../Readme.md)

## Installing RabbitMQ PHP library - `php-amqplib`
Composer needs to be used to install the RabbitMQ library. Here are 3 ways to do this but we use docker composer for this tutorial
```bash
# Replace <command> with install or update 

#1
composer <command>
#2 Composer binary
php composer.phar <command>
#3 Composer Docker
docker run --rm --interactive --tty --volume $PWD:/app composer <command>
```

## Create PHP composer container 
    
```bash
docker pull composer
# downgrade the package version to"=3.0" is needed due to docker composer compatibility issue
# make sure the composer.json file exist

cd ~/Codes/docker-fs/phpRabbitMQ
# due php conflict version, below command is not recommended but we do it just a quick way to make it up and running
docker run --rm --interactive --tty --volume $PWD:/app composer install --ignore-platform-reqs --no-scripts
```

## Running the php RabbitMQ Hello World application

```bash
	docker exec -it phpRabbitMQ /bin/bash
	# Run hello world
	php send.php
	php receive.php
```

# References
	* https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/php/send.php
	* https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/php/receive.php

