from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT_HAI ='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    ye function return karega list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ") for req in requirements]
    
    if HYPHEN_E_DOT_HAI  in requirements:
        requirements.remove(HYPHEN_E_DOT_HAI)   
    
    return requirements
  

setup(
    name='ML_Project',
    version='1.0.0',
    author='Abhay_Shukla',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
