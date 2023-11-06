from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirement]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='project',
    version='0.0.1',
    author='sagar',
    author_email='sagarpatrojsr.1997@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()
)
