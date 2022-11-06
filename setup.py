from gettext import install
from typing import List
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function will dynamically pass the reqiuirements.txt as a list to setup.py to install 
    """
    requirement_list:List[str] = []

    #Assignment 1 
    """
    Write a code to read requirements.txt and append each requirements in setup.py at requirements_list variable
    
    """
    return requirement_list


setup(

    name="sensor",
    version="0.0.1",
    author="amogh",
    author_email="kori.amogh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(), #["pymongo==4.20"],
)