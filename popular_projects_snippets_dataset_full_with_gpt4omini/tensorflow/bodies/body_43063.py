# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py

def wrapper(*unused_args, **unused_kwargs):
    pass

exit(tf_decorator.make_decorator(func, wrapper))
