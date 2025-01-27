# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
with ops.get_default_graph().as_default():
    with testing_utils.run_eagerly_scope(False):
        with test_or_class.test_session(config=config):
            f(test_or_class, *args, **kwargs)
