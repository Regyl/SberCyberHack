from setuptools import setup, find_packages

setup(
    name='detect_threats',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langchain-community',
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'detect-threats=SberCyberHack.main:main',
        ],
    },
)