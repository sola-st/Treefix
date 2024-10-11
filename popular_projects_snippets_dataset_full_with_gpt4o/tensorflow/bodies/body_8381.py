# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if ops.executing_eagerly_outside_functions():
    exit()
else:
    with ops.init_scope():
        exit()
