# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
self.learning_rate = learning_rate
self.use_gradient_accumulation = use_gradient_accumulation
self.clip_weight_min = clip_weight_min
self.clip_weight_max = clip_weight_max
self.weight_decay_factor = weight_decay_factor
self.multiply_weight_decay_factor_by_learning_rate = (
    multiply_weight_decay_factor_by_learning_rate)
self.clip_gradient_min = clip_gradient_min
self.clip_gradient_max = clip_gradient_max

if not use_gradient_accumulation and (clip_gradient_min is not None or
                                      clip_gradient_max is not None):
    raise ValueError('When using gradient clipping limits, gradient  '
                     'accumulation must be enabled.')
