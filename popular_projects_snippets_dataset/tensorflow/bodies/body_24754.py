# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Find dumped tensor data by a certain predicate.

    Args:
      predicate: A callable that takes two input arguments:

        ```python
        def predicate(debug_tensor_datum, tensor):
          # returns a bool
        ```

        where `debug_tensor_datum` is an instance of `DebugTensorDatum`, which
        carries the metadata, such as the `Tensor`'s node name, output slot
        timestamp, debug op name, etc.; and `tensor` is the dumped tensor value
        as a `numpy.ndarray`.
      first_n: (`int`) return only the first n `DebugTensotDatum` instances (in
        time order) for which the predicate returns True. To return all the
        `DebugTensotDatum` instances, let first_n be <= 0.
      device_name: optional device name.
      exclude_node_names: Optional regular expression to exclude nodes with
        names matching the regular expression.

    Returns:
      A list of all `DebugTensorDatum` objects in this `DebugDumpDir` object
       for which predicate returns True, sorted in ascending order of the
       timestamp.
    """
if exclude_node_names:
    exclude_node_names = re.compile(exclude_node_names)

matched_data = []
for device in (self._dump_tensor_data if device_name is None
               else (self._dump_tensor_data[device_name],)):
    for datum in self._dump_tensor_data[device]:
        if exclude_node_names and exclude_node_names.match(datum.node_name):
            continue

        if predicate(datum, datum.get_tensor()):
            matched_data.append(datum)

            if first_n > 0 and len(matched_data) >= first_n:
                exit(matched_data)

exit(matched_data)
