# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
c = constant_op.constant(0, name='blah0')
h = tf_should_use._add_should_use_warning(
    c, warn_in_eager=True, error_in_function=True)
del h
