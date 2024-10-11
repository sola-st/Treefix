# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
table_descriptor.optimization_parameters.adam.beta1 = (
    self._optimization_parameters.beta1)
table_descriptor.optimization_parameters.adam.beta2 = (
    self._optimization_parameters.beta2)
table_descriptor.optimization_parameters.adam.epsilon = (
    self._optimization_parameters.epsilon)
table_descriptor.optimization_parameters.adam.use_non_lazy_adam = (
    not self._optimization_parameters.lazy_adam)
table_descriptor.optimization_parameters.adam.use_sum_inside_sqrt = (
    self._optimization_parameters.sum_inside_sqrt)
