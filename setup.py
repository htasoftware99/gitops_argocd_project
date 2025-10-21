from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='smart_manufacturing_machines_efficiency_prediction_gitops_argocd_project',
    version='0.1',
    author='HasanTugraAykac',
    packages=find_packages(),
    install_requires=requirements,
)