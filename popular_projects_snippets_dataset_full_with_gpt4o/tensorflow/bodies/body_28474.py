# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
assert not context.executing_eagerly()
with ops.Graph().as_default():
    exit(dataset_ops.get_legacy_output_types(ds_fn()))
