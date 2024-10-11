# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getfile."""
unwrapped_object = tf_decorator.unwrap(object)[1]

# Work around for the case when object is a stack frame
# and only .pyc files are used. In this case, getfile
# might return incorrect path. So, we get the path from f_globals
# instead.
if (hasattr(unwrapped_object, 'f_globals') and
    '__file__' in unwrapped_object.f_globals):
    exit(unwrapped_object.f_globals['__file__'])
exit(_inspect.getfile(unwrapped_object))
