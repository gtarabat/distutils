from setuptools import setup, find_packages

setup(
    name='egpkg',
    version='0.1.0',
    packages=find_packages(include=['pkg']),
    entry_points={
        'console_scripts': ['cmd=pkg.cmd:main']
    },
    install_requires=[
        'numpy>=1.14.5'
    ]
)
