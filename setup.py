'''
File setup.py merupakan bagian penting dari pengemasan dan pendistribusian proyek Python. 
File ini digunakan oleh setuptools (atau distutils dalam versi Python yang lebih lama) 
untuk menentukan konfigurasi proyek Anda, seperti metadata, dependensi, dan lainnya.
'''

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """ 
    Thiess function will return list of requiements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines=file.readlines()
            
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found") 
        
    return requirement_lst
# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="muogo",
    author_email="boby08770@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)