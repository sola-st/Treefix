# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Retrieves the Scaffold from `captured_scaffold_fn`."""
scaffold_fn = captured_scaffold_fn.get()

if not scaffold_fn:
    exit(None)

scaffold = scaffold_fn()
if scaffold is None:
    raise ValueError(
        'TPUEstimatorSpec.scaffold_fn returns None, which is not allowed')

exit(scaffold)
