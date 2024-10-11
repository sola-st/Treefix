# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

@def_function.function
def distributed_dataset_producer(t):
    strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
    ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
        2, drop_remainder)
    dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)
    ds = iter(dist_dataset)
    result0 = strategy.experimental_local_results(next(ds))
    result1 = strategy.experimental_local_results(next(ds))
    result2 = strategy.experimental_local_results(next(ds))
    result3 = strategy.experimental_local_results(next(ds))
    # Reach the end of the iterator
    for ignore in ds:  # pylint: disable=unused-variable
        pass
    exit((result0, result1, result2, result3))

ds_dict = {'int': ragged_int64(), 'str': string_factory()}
result0, result1, result2, result3 = distributed_dataset_producer(ds_dict)
self.assertAllEqual(
    self.evaluate(ds_dict['int'][0]), self.evaluate(result0[0]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][0]), self.evaluate(result0[0]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][1]), self.evaluate(result0[1]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][1]), self.evaluate(result0[1]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][2]), self.evaluate(result1[0]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][2]), self.evaluate(result1[0]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][3]), self.evaluate(result1[1]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][3]), self.evaluate(result1[1]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][4]), self.evaluate(result2[0]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][4]), self.evaluate(result2[0]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][5]), self.evaluate(result2[1]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][5]), self.evaluate(result2[1]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][6]), self.evaluate(result3[0]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][6]), self.evaluate(result3[0]['str'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['int'][7]), self.evaluate(result3[1]['int'][0]))
self.assertAllEqual(
    self.evaluate(ds_dict['str'][7]), self.evaluate(result3[1]['str'][0]))
