from setuptools import setup, find_packages

setup(
    name='meu_processador_imagens',
    version='1.0',
    author='Aluno Iniciante',
    description='Meu primeiro pacote para processar imagens',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)
