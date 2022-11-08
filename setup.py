from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    """
	#This function will return list of requirements
    """
    requirement_list:list[str]=[]

    """
    #write a code to read requirements.txt file and append each variable to requirements_list variable
    """
    return requirement_list
setup(
        name='sensor',
        version='0.0.1',
        author='manu',
        author_email='manoharkaranth95@gmail.com',
        packages=find_packages(),
    )