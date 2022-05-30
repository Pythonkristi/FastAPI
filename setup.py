from setuptools import setup

setup(
    name='app-example',
    version='1.0',
    author='Vladimir',
    author_email='paradiseipad@mail.ru',
    description='FastApi app',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
    )