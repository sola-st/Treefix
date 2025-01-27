# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# SparseTensorValue is a named tuple which nest will flatten, so we need
# to guard it to properly handle the structure.
self._structure = nest.get_traverse_shallow_structure(
    lambda x: not is_composite_or_composite_value(x), batch_outs)
batch_outs = nest.flatten_up_to(self._structure, batch_outs)

for batch_element in batch_outs:
    if is_composite_or_composite_value(batch_element):
        # If the output is not a ndarray, it will be either a composite tensor
        # or a composite tensor's Value object. In either case, we can't
        # allocate an array to hold the object - we'll handle it later.
        self.results.append(ConcatAggregator(self.batch_size))
    elif isinstance(batch_element, np.ndarray):
        self.results.append(
            (ConcatAggregator(self.batch_size) if self.use_steps else
             SliceAggregator(self.num_samples, self.batch_size)))
    else:
        # This is not a ndarray, a CompositeTensor, or a CompositeTensorValue.
        # Fail fast rather than trying to concatenate it.
        raise RuntimeError('Attempted to aggregate unsupported object {}.'
                           .format(batch_element))

    self.results[-1].create(batch_element)
