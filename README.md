# How to install a Python package

Create and ectivate an environment
```
python3 -m venv test_env
source test_env/bin/activate
```

Install the package
```
python3 -m pip install -e .
```

From anywhere, run in python
```
from pkg import foo
from pkg.bar import bar

foo.my_print('OK 1')
bar.my_print('OK 2')
```
