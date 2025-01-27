# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
if not context.executing_eagerly():
    init_op = iterator.initializer
    backend.get_session((init_op,)).run(init_op)
