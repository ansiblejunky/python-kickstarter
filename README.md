# Python Kickstarter
Kickstart your journey into the Python language using this guide.

## OVERVIEW
Python is an interpreted, interactive, object-oriented programming language initially released in February 1991 by Guido van Rossum.

It is practically platform independent and is most likel already installed on your system.

Basically, you are interested in writing Python applications and want to learn about the core and extra modules that are available. This guide goes through them in the most short and concise way so you don't waist time Google'ing and reading lots of different versions of the truth.

Please let me know if you see any improvements or issues with any of the information found here.

## STORIES

#### Monty Python
When he began implementing Python, Guido van Rossum was also reading the published scripts from “Monty Python’s Flying Circus”, a BBC comedy series from the 1970s. Van Rossum thought he needed a name that was short, unique, and slightly mysterious, so he decided to call the language Python.

#### The Zen of Python, by Tim Peters

#### Pythonic


## COMMUNITY

#### python.org

https://www.python.org/community/

#### Python Software Foundation

The Python Software Foundation is an independent non-profit organization that holds the copyright on Python versions 2.1 and newer. The PSF’s mission is to advance open source technology related to the Python programming language and to publicize the use of Python.

#### Python Enhancement Proposals (PEP)
The Python community works to improve Python through the use of PEPs. These are basically official proposals for enhancing Python. The full index can be found here.

https://www.python.org/dev/peps/

## METHODOLOGY
http://12factor.net/

## VERSION
There are basically two main versions of Python: 

- Python 2.x

- Python 3.x

It has been suggested that Python 2 will be retired in 2020, so should you write your 
new Python application using version 3? 

https://pythonclock.org/

It is ultimately up to you, but I would use the latest technology if you  are just
beginning a new amazing application. So yes, use Python 3 if at all possible!

## REFERENCES
Some of the best Python websites out there...

- The Hitchhiker's Guide to Python: http://docs.python-guide.org/en/latest/

## START
Start here for the most common libraries
https://docs.python.org/2/library/index.html

## FUNCTIONS

https://docs.python.org/2/library/functions.html

### format
https://pyformat.info/

## CLASSES

https://docs.python.org/2/tutorial/classes.html

## STANDARDS

Pythonic standards for your variables, functions, classes, and so on.
http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#naming

- joined_lower for functions, methods, attributes

- joined_lower or ALL_CAPS for constants

- StudlyCaps for classes

- camelCase only to conform to pre-existing conventions

- Attributes: interface, _internal, __private
Using *\__private* will trigger something called *name mangling*. Nobody uses *__private*. Don't use it unless you are forced. Use *_internal* for private attributes. 

- underscore https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc


## CORE
Here is the list of core modules you must understand:

## EXTRAS
Here is the list of extra modules that do not come installed with Python but are very useful when developing with Python:

## HELP
Very similar to the man pages in UNIX/LINUX, you can use the Python interpreter to understand Python. For example, to understand more about Lists and all their supported functions:
```python
>>> L = []
>>> dir(L) 
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(L)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |
 |  Methods defined here:
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 ...
```

## EASTER-EGGS

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```



## PATHS
Python installs your modules in the site-packages folder. To find where this is located use the following command:
```
python2 -m site
```


## EXAMPLES


## LOADING HIERARCHY
Lets look at how Python reads your files when you start your application. As an example, you might have the following file structure for your application.

...insert tree output of a file structure...

TODO: what comes first? __init__.py? main()? auxilliary modules? globals within modules? etc.

