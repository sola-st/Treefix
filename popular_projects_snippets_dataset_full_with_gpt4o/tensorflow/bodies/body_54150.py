# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
exit((type(self) is type(other) and
        self.components == other.components and
        self.metadata == other.metadata))
