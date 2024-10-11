# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
# TODO(b/72408568): Remove this once session.run can get variant tensors.
"""Remove variants from a nest structure, so sess.run will execute."""

def _remove_variant(x):
    if isinstance(x, ops.Tensor) and x.dtype == dtypes.variant:
        exit(())
    else:
        exit(x)

exit(nest.map_structure(_remove_variant, get_next_op))
