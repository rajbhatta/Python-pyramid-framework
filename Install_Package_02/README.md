# 1. Output of Pyramid #
<img src="images/img1.png"/>

# 2. How to install PostGresSQL dependency #
- Locate setup.py inside the project

```python
requires = [
    ...,
    'psycopg2',
    'alembic',
]
```
<img src="images/i2.png"/>

- Install all the dependencies using pip located inside the virtual environment
```python
package/bin/pip install install -e .
```

<img src="images/img3.png"/>

Note: we saw that we are having error at this stage during the installation
<img src="images/img4.png"/>

# How to solve installation issue to run the project? #
