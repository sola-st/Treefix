# Extracted from https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv
import os
os.environ['VIRTUAL_ENV']
'/some/path/project/venv'

import os
os.environ['VIRTUAL_ENV']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: 'VIRTUAL_ENV'

