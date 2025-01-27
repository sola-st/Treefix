# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Generates a callable that runs the graph.

    Args:
      feed_arrays: List of input tensors to be fed Numpy arrays at runtime.
      feed_symbols: List of input tensors to be fed symbolic tensors at runtime.
      symbol_vals: List of symbolic tensors to be fed to `feed_symbols`.
      session: Session to use to generate the callable.

    Returns:
      Function that runs the graph according to the above options.
    """
# Prepare callable options.
callable_opts = config_pb2.CallableOptions()
# Handle external-data feed.
for x in feed_arrays:
    callable_opts.feed.append(x.name)
if self.feed_dict:
    for key in sorted(self.feed_dict.keys()):
        callable_opts.feed.append(key.name)
    # Handle symbolic feed.
for x, y in zip(feed_symbols, symbol_vals):
    connection = callable_opts.tensor_connection.add()
    if x.dtype != y.dtype:
        y = math_ops.cast(y, dtype=x.dtype)
    from_tensor = _as_graph_element(y)
    if from_tensor is None:
        from_tensor = y
    connection.from_tensor = from_tensor.name  # Data tensor
    connection.to_tensor = x.name  # Placeholder
# Handle fetches.
for x in self.outputs + self.fetches:
    callable_opts.fetch.append(x.name)
# Handle updates.
callable_opts.target.append(self.updates_op.name)
# Handle run_options.
if self.run_options:
    callable_opts.run_options.CopyFrom(self.run_options)
# Create callable.
callable_fn = session._make_callable_from_options(callable_opts)
# Cache parameters corresponding to the generated callable, so that
# we can detect future mismatches and refresh the callable.
self._callable_fn = callable_fn
self._feed_arrays = feed_arrays
self._feed_symbols = feed_symbols
self._symbol_vals = symbol_vals
self._fetches = list(self.fetches)
self._session = session
