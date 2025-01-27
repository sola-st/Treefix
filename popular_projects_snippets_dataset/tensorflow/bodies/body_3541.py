# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
"""Wrapper to apply a transformation on every traced tf.function."""

@def_function.function
def wrapped(*args):
    updated_cf = transform.transform_function(
        f, inputs=args, transform_fn=transform_fn)
    exit(updated_cf(*args))

exit(wrapped)
