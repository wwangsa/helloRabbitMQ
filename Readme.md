# Practice code based on rabbitmq tutorial
[Reference](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)


## Setting up Docker containers
Using 3 docker containers to play around with Hello World - RabbitMQ. Install it with the following order:

1. Create RabbitMQ container
    ```bash
    docker pull rabbitmq:3-management
    docker run -d --hostname my-rabbit --name wso2-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
    ```
    Access the management console on http://localhost:15672/ using default credentials is guest/guest

2. Create PHP FPM 7.4 container
    ```bash
    mkdir -p ~/Codes/docker-fs/phpRabbitMQ
    docker pull php:7.4-apache
    #-d is detached --rm is remove the container upon stop
    #PHP Apache
    docker run -itd --rm -p 8080:80 -v ~/Codes/docker-fs/phpRabbitMQ:/var/www/html --name phpRabbitMQ php:7.4-apache
    # PHP FPM
    #docker run -itd --rm -v ~/Codes/docker-fs/phpRabbitMQ:/var/www/html --name phpRabbitMQ php:7.4-fpm-buster
    ```
    PHP server can be access on http://localhost:8080/ but only command is being used. No web is needed.

3. Create RabbitMQ container 
    
    ```bash
    cd ~/Codes/docker-fs/phpRabbitMQ
	# downgrade the package version due to docker composer compatibility issue
	#vim composer.json
	#{
	#	"require": {
	#		"php-amqplib/php-amqplib": "=3.0"
	#	}
	#}
	docker pull composer
	# Replace <command> with install or update 
	docker run --rm --interactive --tty --volume $PWD:/app composer <command>
	
	# due php conflict version, below command is not recommended but we do it just a quick way to make it up and running
	docker run --rm --interactive --tty --volume $PWD:/app composer install --ignore-platform-reqs --no-scripts
    ```

    RabbitMQ Hello World instructions
    * [Python](pyRabbitMQ/Readme.md)
    * [PHP](phpRabbitMQ/Readme.md)


## References

DockerHub
+ [Composer](https://hub.docker.com/_/composer)
+ [PHP](https://hub.docker.com/_/php)
+ [RabbitMQ](https://hub.docker.com/_/rabbitmq)
