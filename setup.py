from setuptools import find_packages,setup
from typing import List

# its used to run setup by default
HYPEN_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
    """
    this function return list of requirments 
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n',"") for req in requirments]
        
    if HYPEN_DOT in requirments:
        requirments.remove(HYPEN_DOT)

    return  requirments


setup(
name='MLProject',
version='0.0.1',
author='Sanjay',
author_email='sanjayr@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirements.txt')
)
