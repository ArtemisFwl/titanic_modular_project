from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Here I have started to make a new function.
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #simple list comprehension to replace /n with blank

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

'''
When I install requirements.txt, 
setup.py should run automatically.
for this, we have put -e . in requirements.txt
this automatically triggers setup.py

But now we have a problem. 
When we install requirements.txt, -e. will also come 
We do not want this to come. 
For this, while updating the list, it will not be loaded.
we have put condition for this.


'''

setup(
name='Titanic Project',
version='0.0.1',
author='Aman Deep',
author_email='artemisfowl795@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)