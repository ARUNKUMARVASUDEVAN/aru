from setuptools import find_packages,setup
from typing import List

Hyphen_E_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requiremets=[]
    with open(file_path) as f:
        requiremets=f.readlines()
        requiremets=[req.replace("\n","") for req in requiremets]

        if Hyphen_E_dot in requiremets:
            requiremets.remove(Hyphen_E_dot)

    return requiremets


setup(
    name='My project for my practice',
    version='0.0.1',
    author='Arun',
    author_email='arunssvvg@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()


)