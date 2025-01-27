# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
exit(('mask' in self._call_fn_args or
        getattr(self, 'compute_mask', None) is not None))
