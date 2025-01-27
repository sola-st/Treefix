# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
with context.eager_mode():
    with testing_utils.run_eagerly_scope(False):
        f(test_or_class, *args, **kwargs)
