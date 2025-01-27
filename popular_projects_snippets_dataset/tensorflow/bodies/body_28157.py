# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
exit([
    ts.as_list()
    for ts in nest.flatten(dataset_ops.get_legacy_output_shapes(dataset))
])
