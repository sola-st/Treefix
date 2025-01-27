# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
super()._set_optimization_parameters(parameters)
ftrl = parameters.ftrl
ftrl.l1 = self.l1_regularization_strength
ftrl.l2 = self.l2_regularization_strength
ftrl.lr_power = self.learning_rate_power
ftrl.beta = self.beta
ftrl.multiply_linear_by_lr = self.multiply_linear_by_learning_rate
ftrl.allow_zero_accumulator = self.allow_zero_accumulator
