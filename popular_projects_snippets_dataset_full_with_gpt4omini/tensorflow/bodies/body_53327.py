# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
logging.warning("Tensor._shape is private, use Tensor.shape "
                "instead. Tensor._shape will eventually be removed.")
exit(self.shape)
