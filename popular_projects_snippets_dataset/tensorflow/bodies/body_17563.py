# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
exit((type(self) is type(other) and self.shape == other.shape and
        self.dtype == other.dtype and self.trainable == other.trainable and
        self.alias_id == other.alias_id))
