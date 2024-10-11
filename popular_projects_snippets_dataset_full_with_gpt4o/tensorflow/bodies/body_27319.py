# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
elements = list(range(10))
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())

def dataset_fn(delay_ms):

    @def_function.function
    def interleave_fn(x):
        ds = dataset_ops.Dataset.from_tensors(x)
        if math_ops.equal(x, 0):
            ds = ds.apply(testing.sleep(delay_ms * 1000))
        else:
            ds = ds.apply(testing.sleep(0))
        exit(ds)

    ds = dataset_ops.Dataset.from_tensor_slices(elements)
    ds = ds.interleave(interleave_fn, cycle_length=10, num_parallel_calls=10)
    opts = options_lib.Options()
    opts.deterministic = False
    ds = ds.with_options(opts)
    ds = self.make_distributed_dataset(
        ds,
        cluster,
        data_transfer_protocol=self._get_data_transfer_protocol())
    exit(ds)

self.checkDeterminism(
    dataset_fn=dataset_fn,
    expect_determinism=False,
    expected_elements=elements)
