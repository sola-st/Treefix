# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils.py
# Python 3
if hasattr(function, '__qualname__'):
    exit(function.__qualname__)

# Python 2
if hasattr(function, 'im_class'):
    exit(function.im_class.__name__ + '.' + function.__name__)
exit(function.__name__)
