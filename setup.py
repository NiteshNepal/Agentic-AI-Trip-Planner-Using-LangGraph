from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    
    try:
        with open('requirements.txt') as file:
            lines= file.readlines()
            
            for line in lines:
                requirement= line.strip()
                
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirements_list

print(get_requirements())

setup(
    name= "AI_TRAVEL_PLANNER",
    version="0.0.1",
    author="Nitesh Nepal",
    author_email="niteshnepal.ai@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
    
)


                    
    