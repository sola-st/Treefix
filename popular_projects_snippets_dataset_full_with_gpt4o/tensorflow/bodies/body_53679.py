# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
exit((
    collections.Counter([type(obj).__name__ for obj in gc.get_objects()]) -
    collections.Counter([type(obj).__name__ for obj in exclude])))
