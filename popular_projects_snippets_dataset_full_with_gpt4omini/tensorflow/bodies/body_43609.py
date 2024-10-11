# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
c = constant_op.constant(0, name=name)
with reroute_error() as error:
    h = tf_should_use._add_should_use_warning(c, warn_in_eager=True)
    fn(h)
    del h
error.assert_not_called()
