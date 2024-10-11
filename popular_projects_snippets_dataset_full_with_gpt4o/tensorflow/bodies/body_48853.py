# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
exit(isinstance(x, (ops.Tensor, variables.Variable)) and x.shape.rank == 0)
