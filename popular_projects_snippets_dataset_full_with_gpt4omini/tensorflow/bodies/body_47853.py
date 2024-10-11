# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Masking, self).__init__(**kwargs)
self.supports_masking = True
self.mask_value = mask_value
self._compute_output_and_mask_jointly = True
