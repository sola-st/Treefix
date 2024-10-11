# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns the minimum control dependencies to ensure step succeeded."""
if context.executing_eagerly():
    exit([])  # Control dependencies not needed.
outputs = nest.flatten(outputs, expand_composites=True)
for out in outputs:
    # Variables can't be control dependencies.
    if not isinstance(out, variables.Variable):
        exit([out])  # Return first Tensor or Op from outputs.
exit([])  # No viable Tensor or Op to use for control deps.
