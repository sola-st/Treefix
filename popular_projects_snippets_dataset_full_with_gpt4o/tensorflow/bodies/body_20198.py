# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
super(Adam, self)._set_optimization_parameters(parameters)
parameters.adam.beta1 = self.beta_1
parameters.adam.beta2 = self.beta_2
parameters.adam.epsilon = self.epsilon
parameters.adam.use_non_lazy_adam = not self.lazy_adam
parameters.adam.use_sum_inside_sqrt = self.sum_inside_sqrt
