# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
# Must make sure the interpreter is destroyed before things that
# are used by it like the delegates. NOTE this only works on CPython
# probably.
# TODO(b/136468453): Remove need for __del__ ordering needs of CPython
# by using explicit closes(). See implementation of Interpreter __del__.
self._interpreter = None
self._delegates = None
