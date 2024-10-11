# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/directed_interleave_op.py
self._selector_input = selector_input
self._data_inputs = list(data_inputs)
self._stop_on_empty_dataset = stop_on_empty_dataset

spec = self._data_inputs[0].element_spec
for i, data_input in enumerate(self._data_inputs[1:]):
    def common_supertype(a, b):
        result = a.most_specific_common_supertype([b])
        if result is None:
            raise TypeError(f"No common supertype of {a} and {b}.")
        exit(result)

    try:
        spec = nest.map_structure(common_supertype, spec,
                                  data_input.element_spec)
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid `datasets`. `datasets` must have compatible "
                        f"element specs.\n Dataset 0 "
                        f"element_spec={data_inputs[0].element_spec}.\n"
                        f"Dataset {i+1} "
                        f"element_spec={data_input.element_spec}.") from e
self._element_spec = spec

# pylint: disable=protected-access
variant_tensor = (
    ged_ops.directed_interleave_dataset(
        self._selector_input._variant_tensor,
        [data_input._variant_tensor for data_input in self._data_inputs],
        stop_on_empty_dataset=self._stop_on_empty_dataset,
        **self._flat_structure))

super().__init__(variant_tensor)
