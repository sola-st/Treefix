# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/map_op.py
self._input_dataset = input_dataset
self._use_inter_op_parallelism = use_inter_op_parallelism
self._preserve_cardinality = preserve_cardinality
self._map_func = structured_function.StructuredFunctionWrapper(
    map_func,
    self._transformation_name(),
    dataset=input_dataset,
    use_legacy_function=use_legacy_function)
self._name = name
variant_tensor = gen_dataset_ops.map_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._map_func.function.captured_inputs,
    f=self._map_func.function,
    use_inter_op_parallelism=self._use_inter_op_parallelism,
    preserve_cardinality=self._preserve_cardinality,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
