# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
restore_ops = self.restore(file_prefix)
with ops.device("cpu:0"):
    with ops.control_dependencies(restore_ops.values()):
        exit(array_ops.identity(file_prefix))
