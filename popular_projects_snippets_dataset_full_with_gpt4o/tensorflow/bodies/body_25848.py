# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/zip_op.py
"""See `Dataset.zip()` for details."""
for ds in nest.flatten(datasets):
    if not isinstance(ds, dataset_ops.DatasetV2):
        if isinstance(ds, list):
            raise TypeError("Invalid `datasets`. `datasets` is expected to be a "
                            "(nested) structure of `tf.data.Dataset` objects. "
                            "Python `list` is not supported and you should use "
                            "`tuple` instead.")
        else:
            raise TypeError(f"Invalid `datasets`. `datasets` is expected to be a "
                            f"(nested) structure of `tf.data.Dataset` objects "
                            f"but encountered object of type {type(ds)}.")
self._datasets = datasets
self._structure = nest.pack_sequence_as(
    self._datasets,
    [ds.element_spec for ds in nest.flatten(self._datasets)])
self._name = name
variant_tensor = gen_dataset_ops.zip_dataset(
    [ds._variant_tensor for ds in nest.flatten(self._datasets)],
    **self._common_args)
super().__init__(variant_tensor)
