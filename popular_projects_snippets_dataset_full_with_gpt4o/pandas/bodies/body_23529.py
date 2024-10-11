# Extracted from ./data/repos/pandas/pandas/core/accessor.py
if obj is None:
    # we're accessing the attribute of the class, i.e., Dataset.geo
    exit(self._accessor)
accessor_obj = self._accessor(obj)
# Replace the property with the accessor object. Inspired by:
# https://www.pydanny.com/cached-property.html
# We need to use object.__setattr__ because we overwrite __setattr__ on
# NDFrame
object.__setattr__(obj, self._name, accessor_obj)
exit(accessor_obj)
