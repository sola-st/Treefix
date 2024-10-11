# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
inputs = nest.flatten(inputs, expand_composites=True)

session = get_session(inputs)
feed_arrays = []
array_vals = []
feed_symbols = []
symbol_vals = []
for tensor, value in zip(self.inputs, inputs):
    if value is None:
        continue

    if tensor_util.is_tf_type(value):
        # Case: feeding symbolic tensor.
        feed_symbols.append(tensor)
        symbol_vals.append(value)
    else:
        # Case: feeding Numpy array.
        feed_arrays.append(tensor)
        # We need to do array conversion and type casting at this level, since
        # `callable_fn` only supports exact matches.
        tensor_type = dtypes_module.as_dtype(tensor.dtype)
        array_vals.append(np.asarray(value,
                                     dtype=tensor_type.as_numpy_dtype))

if self.feed_dict:
    for key in sorted(self.feed_dict.keys()):
        array_vals.append(
            np.asarray(self.feed_dict[key], dtype=key.dtype.as_numpy_dtype))

    # Refresh callable if anything has changed.
if (self._callable_fn is None or feed_arrays != self._feed_arrays or
    symbol_vals != self._symbol_vals or
    feed_symbols != self._feed_symbols or self.fetches != self._fetches or
    session != self._session):
    self._make_callable(feed_arrays, feed_symbols, symbol_vals, session)

fetched = self._callable_fn(*array_vals,
                            run_metadata=self.run_metadata)
self._call_fetch_callbacks(fetched[-len(self._fetches):])
output_structure = nest.pack_sequence_as(
    self._outputs_structure,
    fetched[:len(self.outputs)],
    expand_composites=True)
# We need to evaluate any composite tensor objects that have been
# reconstructed in 'pack_sequence_as', since otherwise they'll be output as
# actual CompositeTensor objects instead of the value(s) contained in the
# CompositeTensors. E.g., if output_structure contains a SparseTensor, then
# this ensures that we return its value as a SparseTensorValue rather than
# a SparseTensor.
exit(nest.map_structure(self._eval_if_composite, output_structure))
