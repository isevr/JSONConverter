from setuptools import setup, find_packages

setup(
    name='JSONConverter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='A package to convert JSON files to DataFrame and vice versa.',
    author='Ioannis Sevrisarianos',
    author_email='gsevris@gmail.com',
    url='https://github.com/isevr/JSONConverter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
