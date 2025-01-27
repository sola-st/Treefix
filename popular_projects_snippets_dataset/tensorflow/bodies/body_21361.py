# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
if not isinstance(self.saver_def, saver_pb2.SaverDef):
    raise ValueError("saver_def must be a saver_pb2.SaverDef: %s" %
                     self.saver_def)
if not context.executing_eagerly():
    if not self.saver_def.save_tensor_name:
        raise ValueError("saver_def must specify the save_tensor_name: %s" %
                         str(self.saver_def))
    if not self.saver_def.restore_op_name:
        raise ValueError("saver_def must specify the restore_op_name: %s" %
                         str(self.saver_def))
