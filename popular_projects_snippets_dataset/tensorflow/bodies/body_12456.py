# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Create a `SaveSliceInfo`.

      Args:
        full_name: Name of the full variable of which this `Variable` is a
          slice.
        full_shape: Shape of the full variable, as a list of int.
        var_offset: Offset of this `Variable` into the full variable, as a list
          of int.
        var_shape: Shape of this `Variable`, as a list of int.
        save_slice_info_def: `SaveSliceInfoDef` protocol buffer. If not `None`,
          recreates the SaveSliceInfo object its contents. `save_slice_info_def`
          and other arguments are mutually exclusive.
        import_scope: Optional `string`. Name scope to add. Only used when
          initializing from protocol buffer.
      """
if save_slice_info_def:
    assert isinstance(save_slice_info_def, variable_pb2.SaveSliceInfoDef)
    self.full_name = ops.prepend_name_scope(
        save_slice_info_def.full_name, import_scope=import_scope)
    self.full_shape = [i for i in save_slice_info_def.full_shape]
    self.var_offset = [i for i in save_slice_info_def.var_offset]
    self.var_shape = [i for i in save_slice_info_def.var_shape]
else:
    self.full_name = full_name
    self.full_shape = full_shape
    self.var_offset = var_offset
    self.var_shape = var_shape
