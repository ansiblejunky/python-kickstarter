# logging
This section contains all modules related to logging

## overview

## references
General logging:
https://docs.python.org/2/library/logging.html

Logging cookbook:
https://docs.python.org/2/howto/logging-cookbook.html

Good logging practice:
https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

http://docs.python-guide.org/en/latest/writing/logging/

## examples

### Silence Logging
A specific logging level can be silenced by simply changing the level for a logger:
```python
logging.Logger.setLevel()
```

To temporarily disable logging entirely, use the attribute:
```python
logging.Logger.disabled = True
```

### Logging in a Library
Notes for configuring logging for a library are in the logging tutorial. Because the user, not the library, should dictate what happens when a logging event occurs, one admonition bears repeating:

Best practice when instantiating loggers in a library is to only create them using the __name__ global variable: the logging module creates a hierarchy of loggers using dot notation, so using __name__ ensures no name collisions.

Place this in your __init__.py:
```python
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
```

### Logging in an Application
There are 3 main ways to configure a logger (INI file, Dictionary, and Code), but let's do it the best way - using code, so we have more control over the behavior of our logger.
