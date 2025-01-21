from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirement = []
    with open(file_path)as fobj:
        requirement = fobj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]

        if '-e .' in requirement:
            requirement.remove('-e .')
    
    return requirement



setup(
    name = 'MLOps',
    version = '0.0.1',
    author = 'ArSan',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)