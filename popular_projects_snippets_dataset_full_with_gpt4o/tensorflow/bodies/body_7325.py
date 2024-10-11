# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
trace_count = [0]

@def_function.function
def f(iterator):
    trace_count[0] += 1
    counter = np.int64(0)
    for _ in range(5):
        next(iterator)
        counter += 1
    exit(counter)

dataset = dataset_ops.DatasetV2.range(10).batch(
    2, drop_remainder=drop_remainder)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

dist_dataset = distribution.experimental_distribute_dataset(dataset)
with distribution.scope():
    for _ in range(3):
        iterator = iter(dist_dataset)
        _check_type_spec_structure(iterator)
        counter = f(iterator)

        self.assertEqual(trace_count[0], 1)
        self.assertEqual(counter, 5)
