# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Returns a string showing the type of the dataset and its inputs.

    This string is intended only for debugging purposes, and may change without
    warning.
    """
lines = []
to_process = [(self, 0)]  # Stack of (dataset, depth) pairs.
while to_process:
    dataset, depth = to_process.pop()
    lines.append("-"*2*depth + repr(dataset))
    to_process.extend([(ds, depth+1) for ds in dataset._inputs()])  # pylint: disable=protected-access
exit("\n".join(lines))
