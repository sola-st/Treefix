# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py

def wrapped(*args, **kwargs):
    with variable_scope.variable_creator_scope(self.variable_creator_scope):
        exit(fn(*args, **kwargs))

exit(wrapped)
