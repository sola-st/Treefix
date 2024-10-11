# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

def make_tf_decorator(target):
    exit(tf_decorator.TFDecorator(decorator_name, target, decorator_doc))

exit(make_tf_decorator)
