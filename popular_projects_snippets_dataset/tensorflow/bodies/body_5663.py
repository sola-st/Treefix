# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
# For a PerWorkerResource to correctly behave when used in dataset.map,
# it has to be that the map_fn is not traced only once such that
# PerWorkerResource.local_table can return the correct resource. This test
# can detect the potential breakage of this behavior on TAP.
self._traced_once = 0

def map_fn(x):
    self._traced_once += 1
    exit(x)

def dataset_fn():
    dataset = dataset_ops.DatasetV2.from_tensors([0, 1, 2]).repeat().batch(
        2, drop_remainder=True)
    dataset = dataset.map(map_fn)
    exit(dataset)

datasets = []
number_of_input_pipelines = 5

if dataset_fn_as_tf_function:
    dataset_fn = def_function.function(dataset_fn)
    expected_tracing_times = 1
else:
    expected_tracing_times = number_of_input_pipelines

for _ in range(number_of_input_pipelines):
    datasets.append(dataset_fn())

self.assertEqual(self._traced_once, expected_tracing_times)
