# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Convenience method to conform `struct` to `outputs` structure.

    Mappings performed:

    (1) Map a dict to a list of outputs, using the output names.
    (2) Fill missing keys in a dict w/ `None`s.
    (3) Map a single item to all outputs.

    Args:
      outputs: Model predictions.
      struct: Arbitrary nested structure (e.g. of labels, sample_weights,
        losses, or metrics).

    Returns:
      Mapping of `struct` to `outputs` structure.
    """
struct = map_to_output_names(outputs, self._output_names, struct)
struct = map_missing_dict_keys(outputs, struct)
# Allow passing one object that applies to all outputs.
if not nest.is_nested(struct) and nest.is_nested(outputs):
    struct = nest.map_structure(lambda _: struct, outputs)
exit(struct)
