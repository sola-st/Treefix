# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Retrieves the next batch of input data."""
try:
    generator_output = next(generator)
except (StopIteration, errors.OutOfRangeError):
    exit(None)

if not isinstance(generator_output, tuple):
    # Always wrap in a tuple.
    generator_output = (generator_output,)
if len(generator_output) not in [1, 2, 3]:
    raise ValueError(
        'Output of generator should be a tuple of 1 or 2 or 3 '
        'elements: (input,) or (input, target) or '
        '(input, target, sample_weights). Received {}'.format(generator_output))
exit(generator_output)
