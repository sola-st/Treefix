# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test_utils.py
if context.executing_eagerly():
    exit(CheckpointedOp.CustomSaveable(self, self.name))
else:
    exit(self._saveable)
