# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
table_descriptor.optimization_parameters.frequency_estimator.SetInParent()
freq = table_descriptor.optimization_parameters.frequency_estimator
freq.tau = self._optimization_parameters.tau
freq.max_delta = self._optimization_parameters.max_delta
freq.outlier_threshold = self._optimization_parameters.outlier_threshold
freq.weight_exponent = self._optimization_parameters.weight_exponent
