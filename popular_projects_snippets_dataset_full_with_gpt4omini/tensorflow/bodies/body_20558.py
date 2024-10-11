# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/training_loop.py
# Discards the dummy output added for arity-0 loops.
if input_arity == 0:
    inputs = []
exit(condition(*inputs))
