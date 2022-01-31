# How to install locally a Python package for development

Create and activate an environment
```
python3 -m venv test_env
source test_env/bin/activate
```

Install the package
```
python3 -m pip install -e .
```
Installing the package with `-e` allows you to make changes to the code and the changes will be applied directly.

From anywhere, run in python
```
from pkg import foo
from pkg.bar import bar

foo.my_print('OK 1')
bar.my_print('OK 2')
```

From command line, run
```
cmd
```
This functionality is added by the following lines in `setup.py`
```
entry_points={
  console_scripts': ['cmd=pkg.cmd:main']
}
```
