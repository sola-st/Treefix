# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
ActualType = collections.namedtuple('ActualType', ['a', 'b', 'c'])

class MockWrapper(tuple):
    # Generated through trackable data structures:
    # //tensorflow/python/training/tracking/data_structures.py
    # With design pattern similar to Python functools:
    # https://docs.python.org/3/library/functools.html?highlight=__wrapped__#functools.update_wrapper
    __wrapped__ = ActualType(1, 2, 3)

self.assertEqual(
    trace_type.from_value(MockWrapper()),
    trace_type.from_value(ActualType(1, 2, 3)))
