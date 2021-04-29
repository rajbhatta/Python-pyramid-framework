# 1. Creating pyramid Python project #

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd Getting_started_01

- Create a Python virtual environment, if not already created.
  ```java
    python3 -m venv raj
  ```
  
<img src="img/img1.png"/>
<img src="img/img2.png"/>

- Activate created python environment

- Upgrade packaging tools, if necessary.
```java
    raj/bin/pip install --upgrade pip setuptools
``` 

- Install the project in editable mode with its testing requirements.
```java
    raj/bin/pip install -e .
 ```
 
     <img src="img/img4.png"/>

- Run your project's tests.

    raj/bin/pytest

- Run your project.
```java
    raj/bin/pserve development.ini
```

     <img src="img/img5.png"/>
