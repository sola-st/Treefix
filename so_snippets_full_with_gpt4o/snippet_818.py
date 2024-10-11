# Extracted from https://stackoverflow.com/questions/1156023/print-current-call-stack-from-a-method-in-code
from __future__ import print_function
import functools
import traceback
import sys

INDENT = 4*' '

def stacktrace(func):
    @functools.wraps(func)
    def wrapped(*args, **kwds):
        # Get all but last line returned by traceback.format_stack()
        # which is the line below.
        callstack = '\n'.join([INDENT+line.strip() for line in traceback.format_stack()][:-1])
        print('{}() called:'.format(func.__name__))
        print(callstack)
        return func(*args, **kwds)

    return wrapped

@stacktrace
def test_func():
    return 42

print(test_func())

test_func() called:
    File "stacktrace_decorator.py", line 28, in <module>
    print(test_func())
42

