# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Creates a new `StructuredTensor` with the updated fields.

    If this `StructuredTensor` is a scalar, and `k` is the `FieldName` being
    updated and `v` the new value, then:

    ```
    result[k] = v              # If (k, v) is in updates and v is a FieldValue
    result[k] = f(self[k])     # If (k, f) is in updates and f is a FieldFn
    result[k] = self[k]        # If k is in self.field_names but not in updates
    ```

    If this `StructuredTensor` has rank `N` and shape `[D1...DN]`, then each
    FieldValue `v` in `updates` must have shape `[D1...DN, ...]`, that is,
    prefixed with the same shape as the `StructuredTensor`. Then the resulting
    `StructuredTensor` will have:

    ```
    result[i1...iN][k] = v[i1...iN]                        # (k, v) in updates
    result[i1...iN][k] = f(self.field_value(k))[i1...iN]   # (k, f) in updates
    result[i1...iN][k] = self[i1...iN][k]                  # k not in updates
    ```

    Note that `result.shape` is always equal to `self.shape` (but the shapes
    of nested StructuredTensors may be changed if they are updated with new
    values).

    Args:
      updates: A dictionary mapping `FieldName` to either a `FieldValue` to be
        used to update, or a `FieldFn` that will transform the value for the
        given `FieldName`. `FieldName` can be a string for a direct field, or a
        sequence of strings to refer to a nested sub-field. `FieldFn` is a
        function that takes a `FieldValue` as input and should return a
        `FieldValue`. All other fields are copied over to the new
        `StructuredTensor`. New `FieldName` can be given (to add new fields),
        but only to existing `StructuredTensor`, it won't automatically create
        new nested structures -- but one can create a whole `StructureTensor`
        sub-structure and set that into an existing structure. If the new value
        is set to `None`, it is removed.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `shape.rank`
        dimensions.

    Returns:
      A `StructuredTensor`.

    Raises:
      `ValueError`: If the any of the `FieldName` keys points to non-existent
        sub-structures, if parent and child nodes are updated, if shapes
        change, if a delete update is given for a non-existent field, or if a
        `FieldFn` transforming function is given for a `FieldName` that doesn't
        yet exist.

    Examples:

    >>> shoes_us = tf.experimental.StructuredTensor.from_pyval([
    ...    {"age": 12, "nicknames": ["Josaphine"],
    ...       "shoes": {"sizes": [8.0, 7.5, 7.5]}},
    ...    {"age": 82, "nicknames": ["Bob", "Bobby"],
    ...        "shoes": {"sizes": [11.0, 11.5, 12.0]}},
    ...    {"age": 42, "nicknames": ["Elmo"],
    ...        "shoes": {"sizes": [9.0, 9.5, 10.0]}}])
    >>> def us_to_europe(t):
    ...   return tf.round(t * 2.54 + 17.0)  # Rough approximation.
    >>> shoe_sizes_key = ("shoes", "sizes")
    >>> shoes_eu = shoes_us.with_updates({shoe_sizes_key: us_to_europe})
    >>> shoes_eu.field_value(shoe_sizes_key)
    <tf.RaggedTensor [[37.0, 36.0, 36.0], [45.0, 46.0, 47.0],
    [40.0, 41.0, 42.0]]>
    """
updates_items = [(_normalize_field_name_to_tuple(name), value)
                 for name, value in updates.items()]

# Sort by keys and check for updates of both parent and child nodes.
updates_items = sorted(updates_items)
for i in range(1, len(updates_items)):
    # Parent of a node would precede node in the sorted order.
    name = updates_items[i][0]  # item[0] is the name, item[1] is the value.
    prev_name = updates_items[i - 1][0]
    if name[:len(prev_name)] == prev_name:
        raise ValueError(
            '`StructuredTensor.with_updates` does not allow both parent and '
            'child nodes to be updated: parent={}, child={}. If needed you can '
            'update child nodes in the parent update value.'.format(
                prev_name, name))
exit(self._with_updates_impl((), updates_items, validate))
