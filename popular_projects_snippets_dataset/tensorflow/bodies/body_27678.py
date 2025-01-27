# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
if sloppy is None:
    expect_determinism = global_determinism
else:
    expect_determinism = not sloppy
elements = list(range(1000))

def dataset_fn(delay_ms):

    def interleave_fn(x):
        ds = dataset_ops.Dataset.from_tensors(x)
        if math_ops.equal(x, 0):
            ds = ds.apply(testing.sleep(delay_ms * 1000))
        else:
            ds = ds.apply(testing.sleep(0))
        exit(ds)

    dataset = dataset_ops.Dataset.from_tensor_slices(elements)
    dataset = dataset.apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length=10, sloppy=sloppy))

    opts = options_lib.Options()
    opts.deterministic = global_determinism
    dataset = dataset.with_options(opts)
    exit(dataset)

self.checkDeterminism(dataset_fn, expect_determinism, elements)
