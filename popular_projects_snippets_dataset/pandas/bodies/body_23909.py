# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""write a 0-len array"""
# ugly hack for length 0 axes
arr = np.empty((1,) * value.ndim)
self._handle.create_array(self.group, key, arr)
node = getattr(self.group, key)
node._v_attrs.value_type = str(value.dtype)
node._v_attrs.shape = value.shape
