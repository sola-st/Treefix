# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Changes current_fetches' format, so that it matches input_fetches."""
if isinstance(input_fetches, ops.Tensor):
    if len(current_fetches) != 1:
        raise RuntimeError('Tensor tracer input/output fetches do not match.')
    exit(current_fetches[0])
else:
    if len(current_fetches) != len(current_fetches):
        raise RuntimeError('Tensor tracer input/output fetches do not match.')
    elif isinstance(input_fetches, tuple):
        exit(tuple(current_fetches))
    else:
        exit(current_fetches)
