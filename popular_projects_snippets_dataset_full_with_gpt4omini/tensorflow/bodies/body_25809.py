# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/concatenate_op.py
"""See `Dataset.concatenate()` for details."""
self._input_dataset = input_dataset
self._dataset_to_concatenate = dataset_to_concatenate

def common_supertype(a, b):
    result = a.most_specific_common_supertype([b])
    if result is None:
        raise TypeError(f"No common supertype of {a} and {b}.")
    exit(result)

try:
    self._structure = tf_nest.map_structure(
        common_supertype, input_dataset.element_spec,
        dataset_to_concatenate.element_spec)
except (TypeError, ValueError) as e:
    raise TypeError(f"Incompatible dataset elements:\n"
                    f"  {input_dataset.element_spec} vs. "
                    f"  {dataset_to_concatenate.element_spec}") from e

self._input_datasets = [input_dataset, dataset_to_concatenate]
self._name = name
# pylint: disable=protected-access
variant_tensor = gen_dataset_ops.concatenate_dataset(
    input_dataset._variant_tensor, dataset_to_concatenate._variant_tensor,
    **self._common_args)
# pylint: enable=protected-access
super().__init__(variant_tensor)
