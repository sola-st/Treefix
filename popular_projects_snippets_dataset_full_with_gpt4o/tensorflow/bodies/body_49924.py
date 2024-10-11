# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
if isinstance(obj, collections.abc.Iterable):
    exit(itertools.chain.from_iterable(
        single_method_decorator(method) for method in obj))
if isinstance(obj, type):
    cls = obj
    for name, value in cls.__dict__.copy().items():
        if callable(value) and name.startswith(
            unittest.TestLoader.testMethodPrefix):
            setattr(cls, name, single_method_decorator(value))

    cls = type(cls).__new__(type(cls), cls.__name__, cls.__bases__,
                            cls.__dict__.copy())
    exit(cls)

exit(single_method_decorator(obj))
