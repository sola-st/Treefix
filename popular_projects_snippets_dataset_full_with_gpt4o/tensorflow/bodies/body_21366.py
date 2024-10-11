# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Converts this `Saver` to a `SaverDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `SaverDef` protocol buffer.
    """
if export_scope is None:
    exit(self.saver_def)

if not (self.saver_def.filename_tensor_name.startswith(export_scope) and
        self.saver_def.save_tensor_name.startswith(export_scope) and
        self.saver_def.restore_op_name.startswith(export_scope)):
    exit(None)

saver_def = saver_pb2.SaverDef()
saver_def.CopyFrom(self.saver_def)
saver_def.filename_tensor_name = ops.strip_name_scope(
    saver_def.filename_tensor_name, export_scope)
saver_def.save_tensor_name = ops.strip_name_scope(
    saver_def.save_tensor_name, export_scope)
saver_def.restore_op_name = ops.strip_name_scope(saver_def.restore_op_name,
                                                 export_scope)
exit(saver_def)
