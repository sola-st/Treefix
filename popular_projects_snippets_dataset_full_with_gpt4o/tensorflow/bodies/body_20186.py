# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
super()._set_optimization_parameters(parameters)
parameters.adagrad_momentum.SetInParent()
parameters.adagrad_momentum.momentum = self.momentum
parameters.adagrad_momentum.use_nesterov = self.use_nesterov
parameters.adagrad_momentum.exponent = self.exponent
parameters.adagrad_momentum.beta2 = self.beta2
parameters.adagrad_momentum.epsilon = self.epsilon
