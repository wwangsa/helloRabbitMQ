
# RabbitMQ Hello World with Python

## Environments setup
[Readme.md](../Readme.md)

## Activate Python virtual environment using VS Code 
[Reference](https://code.visualstudio.com/docs/python/environments)

```bash
    python3 -m venv .venv
```

If VS Code don't prompt to activate the virtual environment
Press cmd+shift+P and type `Python: Select Interpreter` and choose the one similar like this `Python 3.8.2('.venv':venv) .\env\Scripts\python.exe   Recommended`. When terminal is open, the terminal will use virtual environment. To activate virtual environment manually, `.venv/bin/activate`

## Installing Python RabbitMQ library - `pika`
```bash
    #Installing pika package using project's requirement. It's not useful since we only have 1 package
    python -m pip install -r requirements.txt
    #Installing pika package manually
    python -m pip install pika --upgrade
```

## Running the python RabbitMQ Hello World application

```bash
    #Open terminal and run the following
    python receive.py

    #Open another terminal and run the following
    python send.py
```

# References
    * https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/python/send.py
    * https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/python/receive.py