# extracted from https://docs-old.fedoraproject.org/ro/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch-rpm-programming-python.html

TODO: fix this text

Python supports a number of different toolkits for creating graphical user interfaces. You need one of these toolkits if you want to create Python applications that sport a user interface instead of command-line tools. Among the most popular toolkits are PyGKT, PyQt, and Tkinter.
*PyGTK is a binding between Python and the GTK+ toolkit used by the GNOME desktop, one of two main desktop environments for Linux. (KDE is the other main desktop environment.) The Red Hat redhat-config-packages program uses PyGTK and sports a very good-looking user interface.
PyGTK provides full access to the GTK+ widgets such as menus, dialog windows, and buttons. Install the pygtk2 module for PyGTK. For more on PyGTK, see www.daa.com.au/~james/pygtk/.
*PyQt connects Python scripts to the Qt C++ user interface toolkit. Qt forms the base library used by the KDE desktop environment and KDE applications. As with PyGTK, PyQt allows you to access the rich widget set provided by the library.
Install the PyQt package for PyQt. For more on PyQt, see www.riverbankcomputing.co.uk/pyqt/.
*Tkinter is considered a standard part of Python and is based on the Tk (pronounced teekay) toolkit from the Tcl scripting language. The main advantages of Tkinter are that it is considered part of Python, meaning users are more likely to have it, and Tkinter works on multiple platforms, including Windows.
The main drawback of Tkinter is that the widget sets are not as rich as PyQt or PyGTK. For more on Tkinter, see www.python.org/topics/tkinter/.
After you’ve set up your environment and installed all the necessary packages, the next step is to start working with the Python API for RPM.

## overview
Python has many different GUI tookkits available. The point here is not to cover every single one, but rather to focus on those that I feel are much more interesting. I like to keep things simple - go with one solution until you need to use a different one. 

If you are interested, you can find a list of other toolkits:
https://docs.python.org/3/faq/gui.html

### kivy
https://kivy.org/
Open source Python library for rapid development of applications that makes use of innovative user interfaces, such as multi-touch apps.

Kivy runs on Linux, Windows, OS X, Android, iOS, and Raspberry Pi. You can run the same code on all supported platforms. It can natively use most inputs, protocols and devices including WM_Touch, WM_Pen, Mac OS X Trackpad and Magic Mouse, Mtdev, Linux Kernel HID, TUIO. A multi-touch mouse simulator is included.

A simple 'Hello World' app is incredibly easy to create:
```python
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
```