# Extracted from https://stackoverflow.com/questions/3702675/how-to-catch-and-print-the-full-exception-traceback-without-halting-exiting-the
import traceback

''.join(traceback.format_exception(None, exc_obj, exc_obj.__traceback__))

#!/usr/bin/env python3

import traceback

def f():
    g()

def g():
    raise Exception('asdf')

try:
    g()
except Exception as e:
    exc_obj = e

tb_str = ''.join(traceback.format_exception(None, exc_obj, exc_obj.__traceback__))
print(tb_str)

Traceback (most recent call last):
  File "./main.py", line 12, in <module>
    g()
  File "./main.py", line 9, in g
    raise Exception('asdf')
Exception: asdf

