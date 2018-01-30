## overview
This section contains all modules related to processes

## modules

### sh
sh is a full-fledged subprocess replacement for Python 2.6 - 3.6, PyPy and PyPy3 that allows you to call any program as if it were a function
https://pypi.python.org/pypi/sh
https://github.com/amoffat/sh
http://amoffat.github.io/sh/

### sub-process

## references

## examples
```python
from sh import ifconfig
print ifconfig("eth0")
```