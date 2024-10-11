# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
self.learning_rate = learning_rate
self.use_gradient_accumulation = use_gradient_accumulation
self.clip_weight_min = clip_weight_min
self.clip_weight_max = clip_weight_max
if not use_gradient_accumulation and clipvalue is not None:
    raise ValueError(
        f"When `use_gradient_accumulation` is False, gradient clipping "
        f"cannot be used and `clipvalue` should be left as None. "
        f"Received value {clipvalue} for argument `clipvalue`.")
if clipvalue is None:
    clipvalue = (None, None)
elif not isinstance(clipvalue, tuple):
    clipvalue = (-1. * clipvalue, clipvalue)
self.clip_gradient_min, self.clip_gradient_max = clipvalue

self.weight_decay_factor = weight_decay_factor
self.multiply_weight_decay_factor_by_learning_rate = (
    multiply_weight_decay_factor_by_learning_rate)

if (slot_variable_creation_fn is not None and
    not callable(slot_variable_creation_fn)):
    raise ValueError(
        f"Argument `slot_variable_creation_fn` must be either None or a "
        f"callable. Received: {slot_variable_creation_fn}")
self.slot_variable_creation_fn = slot_variable_creation_fn
self.low_dimensional_packing_status = low_dimensional_packing_status
