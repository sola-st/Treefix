# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/batching.py
self._input_dataset = input_dataset

self._map_func = structured_function.StructuredFunctionWrapper(
    map_func,
    "tf.data.experimental.map_and_batch()",
    dataset=input_dataset,
    use_legacy_function=use_legacy_function)
self._batch_size_t = ops.convert_to_tensor(
    batch_size, dtype=dtypes.int64, name="batch_size")
self._num_parallel_calls_t = ops.convert_to_tensor(
    num_parallel_calls, dtype=dtypes.int64, name="num_parallel_calls")
self._drop_remainder_t = ops.convert_to_tensor(
    drop_remainder, dtype=dtypes.bool, name="drop_remainder")

constant_drop_remainder = tensor_util.constant_value(self._drop_remainder_t)
# pylint: disable=protected-access
if constant_drop_remainder:
    # NOTE(mrry): `constant_drop_remainder` may be `None` (unknown statically)
    # or `False` (explicitly retaining the remainder).
    # pylint: disable=g-long-lambda
    self._element_spec = nest.map_structure(
        lambda component_spec: component_spec._batch(
            tensor_util.constant_value(self._batch_size_t)),
        self._map_func.output_structure)
else:
    self._element_spec = nest.map_structure(
        lambda component_spec: component_spec._batch(None),
        self._map_func.output_structure)
# pylint: enable=protected-access
variant_tensor = ged_ops.map_and_batch_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,
    f=self._map_func.function,
    batch_size=self._batch_size_t,
    num_parallel_calls=self._num_parallel_calls_t,
    drop_remainder=self._drop_remainder_t,
    preserve_cardinality=True,
    **self._flat_structure)
super(_MapAndBatchDataset, self).__init__(input_dataset, variant_tensor)
