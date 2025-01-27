# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
ds = dataset_ops.Dataset.from_tensors(x)
if math_ops.equal(x, 0):
    ds = ds.apply(testing.sleep(delay_ms * 1000))
else:
    ds = ds.apply(testing.sleep(0))
exit(ds)
