'''
This setup.py file is an essential part of packagin and distributing Python Projects.
it is used by setup tools to define the configuration of your projects such as metadata,
dependancies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read line from the file
            line=file.readlines()
            #process each line 
            for lines in line:
                requirement=lines.strip()
                #ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                     requirement_list.append(requirement)
    except FileNotFoundError:
        print("File not found")
    return requirement_list

print(get_requirments())     


setup(
    name="Network_Security_system",
    version="0.0.1",
    author="Krish Naik",
    author_email="jeevanaher732@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
)
