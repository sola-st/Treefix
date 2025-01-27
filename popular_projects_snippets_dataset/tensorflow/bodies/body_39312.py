# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
save_op = self.save(file_prefix)
with ops.device("cpu:0"):
    with ops.control_dependencies([save_op]):
        exit(array_ops.identity(file_prefix))
