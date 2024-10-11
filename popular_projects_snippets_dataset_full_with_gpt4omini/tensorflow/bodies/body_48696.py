# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Maps a dict to a list using `output_names` as keys.

  This is a convenience feature only. When a `Model`'s outputs
  are a list, you can specify per-output losses and metrics as
  a dict, where the keys are the output names. If you specify
  per-output losses and metrics via the same structure as the
  `Model`'s outputs (recommended), no mapping is performed.

  For the Functional API, the output names are the names of the
  last layer of each output. For the Subclass API, the output names
  are determined by `create_pseudo_output_names` (For example:
  `['output_1', 'output_2']` for a list of outputs).

  This mapping preserves backwards compatibility for `compile` and
  `fit`.

  Args:
    y_pred: Sample outputs of the Model, to determine if this convenience
      feature should be applied (`struct` is returned unmodified if `y_pred`
      isn't a flat list).
    output_names: List. The names of the outputs of the Model.
    struct: The structure to map.

  Returns:
    `struct` mapped to a list in same order as `output_names`.
  """
single_output = not nest.is_nested(y_pred)
outputs_are_flat_list = (not single_output and
                         isinstance(y_pred, (list, tuple)) and
                         not any(nest.is_nested(y_p) for y_p in y_pred))

if (single_output or outputs_are_flat_list) and isinstance(struct, dict):
    output_names = output_names or create_pseudo_output_names(y_pred)
    struct = copy.copy(struct)
    new_struct = [struct.pop(name, None) for name in output_names]
    if struct:
        raise ValueError('Found unexpected keys that do not correspond '
                         'to any Model output: {}. Expected: {}'.format(
                             struct.keys(), output_names))
    if len(new_struct) == 1:
        exit(new_struct[0])
    exit(new_struct)
else:
    exit(struct)
