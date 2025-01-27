# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Perform either run or partial_run, depending the presence of `handle`."""

def _feed_fn(feed, feed_val):
    for tensor_type, _, feed_fn, _ in _REGISTERED_EXPANSIONS:
        if isinstance(feed, tensor_type):
            exit(feed_fn(feed, feed_val))
    raise TypeError(f'{feed} in argument `feed_dict` has invalid type '
                    f'"{type(feed).__name__}"')

# Check session.
if self._closed:
    raise RuntimeError('Attempted to use a closed Session.')
if self.graph.version == 0:
    raise RuntimeError('The Session graph is empty. Add operations to the '
                       'graph before calling run().')

# Create request.
feed_dict_tensor = {}
feed_map = {}

# Validate and process feed_dict.
feed_handles = {}
if feed_dict:
    feed_dict = nest.flatten_dict_items(feed_dict)
    for feed, feed_val in feed_dict.items():
        for subfeed, subfeed_val in _feed_fn(feed, feed_val):
            try:
                subfeed_t = self.graph.as_graph_element(
                    subfeed, allow_tensor=True, allow_operation=False)
            except Exception as e:
                raise TypeError(
                    f'Cannot interpret feed_dict key as Tensor: {e.args[0]}')

            if isinstance(subfeed_val, ops.Tensor):
                raise TypeError(
                    'The value of a feed cannot be a tf.Tensor object. Acceptable '
                    'feed values include Python scalars, strings, lists, numpy '
                    'ndarrays, or TensorHandles. For reference, the tensor object '
                    f'was {str(feed_val)} which was passed to the argument '
                    f'`feed_dict` with key {str(feed)}.')

            subfeed_dtype = subfeed_t.dtype.as_numpy_dtype
            if isinstance(subfeed_val, int) and _convert_to_numpy_obj(
                subfeed_dtype, subfeed_val) != subfeed_val:
                raise TypeError(
                    f'Type of feed value {str(subfeed_val)} with type ' +
                    f'{str(type(subfeed_val))} is not compatible with Tensor type '
                    f'{str(subfeed_dtype)}. Try explicitly setting the type of the '
                    'feed tensor to a larger type (e.g. int64).')

            is_tensor_handle_feed = isinstance(subfeed_val,
                                               session_ops.TensorHandle)
            if is_tensor_handle_feed:
                np_val = subfeed_val.to_numpy_array()
                feed_handles[subfeed_t.ref()] = subfeed_val
            else:
                np_val = np.asarray(subfeed_val, dtype=subfeed_dtype)

            if (not is_tensor_handle_feed and
                not subfeed_t.get_shape().is_compatible_with(np_val.shape)):
                raise ValueError(
                    f'Cannot feed value of shape {str(np_val.shape)} for Tensor '
                    f'{subfeed_t.name}, which has shape '
                    f'{str(subfeed_t.get_shape())}')
            if not self.graph.is_feedable(subfeed_t):
                raise ValueError(f'Tensor {subfeed_t.name} may not be fed.')

            feed_dict_tensor[subfeed_t.ref()] = np_val
            feed_map[compat.as_bytes(subfeed_t.name)] = (subfeed_t, subfeed_val)

    # Create a fetch handler to take care of the structure of fetches.
fetch_handler = _FetchHandler(
    self._graph, fetches, feed_dict_tensor, feed_handles=feed_handles)

# Run request and get response.
# We need to keep the returned movers alive for the following _do_run().
# These movers are no longer needed when _do_run() completes, and
# are deleted when `movers` goes out of scope when this _run() ends.
# TODO(yuanbyu, keveman): Revisit whether we should just treat feeding
# of a handle from a different device as an error.
_ = self._update_with_movers(feed_dict_tensor, feed_map)
final_fetches = fetch_handler.fetches()
final_targets = fetch_handler.targets()
# We only want to really perform the run if fetches or targets are provided,
# or if the call is a partial run that specifies feeds.
if final_fetches or final_targets or (handle and feed_dict_tensor):
    results = self._do_run(handle, final_targets, final_fetches,
                           feed_dict_tensor, options, run_metadata)
else:
    results = []
exit(fetch_handler.build_results(self, results))
