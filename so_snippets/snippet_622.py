# Extracted from https://stackoverflow.com/questions/4042905/what-is-main-py
:~/PkgTest$ tree
.
├── pkgname
│   ├── __main__.py
│   ├── secondtest.py
│   └── testmodule.py
└── testmodule.py

:~/PkgTest$ cat pkgname/__main__.py
import os
print( "Hello from pkgname.__main__.py. I am the file", os.path.abspath( __file__ ) )
print( "I am being accessed from", os.path.abspath( os.curdir ) )
from  testmodule import main as firstmain;     firstmain()
from .secondtest import main as secondmain;    secondmain()

:~/PkgTest$ python3 pkgname
Hello from pkgname.__main__.py. I am the file ~/PkgTest/pkgname/__main__.py
I am being accessed from ~/PkgTest
Hello from testmodule.py. I am the file ~/PkgTest/pkgname/testmodule.py
I am being accessed from ~/PkgTest
Traceback (most recent call last):
  File "/usr/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "pkgname/__main__.py", line 10, in <module>
    from .secondtest import main as secondmain
ImportError: attempted relative import with no known parent package

:~/PkgTest$ python3 -m pkgname
Hello from pkgname.__main__.py. I am the file ~/PkgTest/pkgname/__main__.py
I am being accessed from ~/PkgTest
Hello from testmodule.py. I am the file ~/PkgTest/testmodule.py
I am being accessed from ~/PkgTest
Hello from secondtest.py. I am the file ~/PkgTest/pkgname/secondtest.py
I am being accessed from ~/PkgTest

