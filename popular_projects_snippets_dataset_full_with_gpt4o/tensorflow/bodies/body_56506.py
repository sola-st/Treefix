# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Return a TraceableObject like this one, but without the object."""
exit(self.__class__(None, filename=self.filename, lineno=self.lineno))
