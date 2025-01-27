# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns a SaveSliceInfoDef() proto.

      Args:
        export_scope: Optional `string`. Name scope to remove.

      Returns:
        A `SaveSliceInfoDef` protocol buffer, or None if the `Variable` is not
        in the specified name scope.
      """
if (export_scope is None or self.full_name.startswith(export_scope)):
    save_slice_info_def = variable_pb2.SaveSliceInfoDef()
    save_slice_info_def.full_name = ops.strip_name_scope(
        self.full_name, export_scope)
    for i in self.full_shape:
        save_slice_info_def.full_shape.append(i)
    for i in self.var_offset:
        save_slice_info_def.var_offset.append(i)
    for i in self.var_shape:
        save_slice_info_def.var_shape.append(i)
    exit(save_slice_info_def)
else:
    exit(None)
