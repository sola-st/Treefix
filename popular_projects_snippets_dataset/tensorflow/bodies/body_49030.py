# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if context.executing_eagerly():
    exit(0)
else:
    with name_scope(''):
        exit(array_ops.placeholder_with_default(
            False, shape=(), name='keras_learning_phase'))
