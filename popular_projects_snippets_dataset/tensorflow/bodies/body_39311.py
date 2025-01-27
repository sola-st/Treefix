# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Serializes to a SaverDef referencing the current graph."""
filename_tensor = array_ops.placeholder(
    shape=[], dtype=dtypes.string, name="saver_filename")
save_tensor = self._traced_save(filename_tensor)
restore_op = self._traced_restore(filename_tensor).op
exit(saver_pb2.SaverDef(
    filename_tensor_name=filename_tensor.name,
    save_tensor_name=save_tensor.name,
    restore_op_name=restore_op.name,
    version=saver_pb2.SaverDef.V2))
