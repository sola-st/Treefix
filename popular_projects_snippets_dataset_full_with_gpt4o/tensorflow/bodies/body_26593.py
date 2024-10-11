# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""See `assert_next()` for details."""
self._input_dataset = input_dataset
if transformations is None:
    raise ValueError(
        "Invalid `transformations`. `transformations` should not be empty.")

self._transformations = ops.convert_to_tensor(
    transformations, dtype=dtypes.string, name="transformations")
variant_tensor = (
    gen_experimental_dataset_ops.experimental_assert_next_dataset(
        self._input_dataset._variant_tensor,  # pylint: disable=protected-access
        self._transformations,
        **self._flat_structure))
super(_AssertNextDataset, self).__init__(input_dataset, variant_tensor)
