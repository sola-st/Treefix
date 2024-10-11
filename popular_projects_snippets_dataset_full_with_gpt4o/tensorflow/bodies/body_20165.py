# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Sets the optimizer fields in the OptimizationParameters."""
if self.use_gradient_accumulation:
    parameters.gradient_accumulation_status = (
        optimization_parameters_pb2.GradientAccumulationStatus.ENABLED)
else:
    parameters.gradient_accumulation_status = (
        optimization_parameters_pb2.GradientAccumulationStatus.DISABLED)

if self.clip_weight_min is not None:
    parameters.clipping_limits.lower.value = self.clip_weight_min

if self.clip_weight_max is not None:
    parameters.clipping_limits.upper.value = self.clip_weight_max

if self.clip_gradient_min is not None:
    parameters.gradient_clipping_limits.lower.value = self.clip_gradient_min

if self.clip_gradient_max is not None:
    parameters.gradient_clipping_limits.upper.value = self.clip_gradient_max

if self.weight_decay_factor:
    parameters.weight_decay_factor = self.weight_decay_factor
    if self.multiply_weight_decay_factor_by_learning_rate:
        parameters.multiply_weight_decay_factor_by_learning_rate = True

parameters.low_dimensional_packing_status = (
    self.low_dimensional_packing_status
)
