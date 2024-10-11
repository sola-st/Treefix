# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/snapshot_op.py

if reader_func is None:
    reader_func = lambda datasets: datasets.interleave(  # pylint:disable=g-long-lambda
        lambda x: x,
        cycle_length=multiprocessing.cpu_count(),
        num_parallel_calls=dataset_ops.AUTOTUNE)

self._input_dataset = input_dataset
self._path = path
self._compression = compression

self._reader_func = structured_function.StructuredFunctionWrapper(
    reader_func,
    self._transformation_name() + ".reader_func",
    # Dataset of datasets of input elements
    input_structure=dataset_ops.DatasetSpec(
        dataset_ops.DatasetSpec(input_dataset.element_spec)),
    use_legacy_function=use_legacy_function)
self._shard_func = structured_function.StructuredFunctionWrapper(
    shard_func,
    self._transformation_name() + ".shard_func",
    dataset=input_dataset,
    use_legacy_function=use_legacy_function)

if ((not self._shard_func.output_structure.is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.int32))) and
    (not self._shard_func.output_structure.is_compatible_with(
        tensor_spec.TensorSpec([], dtypes.int64)))):
    raise TypeError(f"Invalid `shard_func`. `shard_func` must return "
                    f"`tf.int64` scalar tensor but its return type is "
                    f"{self._shard_func.output_structure}.")

self._name = name
variant_tensor = ged_ops.snapshot_dataset_v2(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    path,
    self._reader_func.function.captured_inputs,
    self._shard_func.function.captured_inputs,
    compression=compression,
    reader_func=self._reader_func.function,
    shard_func=self._shard_func.function,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
