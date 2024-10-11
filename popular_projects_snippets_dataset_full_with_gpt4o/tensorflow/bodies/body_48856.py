# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
if ops.inside_function():
    error_msg = (
        'Detected a call to `Model.{method_name}` inside a `tf.function`. '
        '`Model.{method_name} is a high-level endpoint that manages its own '
        '`tf.function`. Please move the call to `Model.{method_name}` outside '
        'of all enclosing `tf.function`s. Note that you can call a `Model` '
        'directly on `Tensor`s inside a `tf.function` like: `model(x)`.'
    ).format(method_name=method_name)
    raise RuntimeError(error_msg)
