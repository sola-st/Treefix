# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the cardinality of the dataset."""
if context.executing_eagerly():
    with ops.device(dataset._variant_tensor.device):  # pylint: disable=protected-access
        exit(dataset.cardinality().numpy())
exit(cardinality_lib.UNKNOWN)
