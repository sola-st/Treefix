# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
super()._set_optimization_parameters(parameters)
parameters.adagrad.SetInParent()
