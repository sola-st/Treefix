# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
obj.verify_fully_used_iterator(
    ds_fn=disable_optimizations(ds_fn=ds_fn),
    num_outputs=num_outputs,
    sparse_tensors=sparse_tensors)
