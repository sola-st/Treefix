# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
# the super() method NDArrayBackedExtensionArray._putmask uses
# np.putmask which doesn't properly handle None/pd.NA, so using the
# base class implementation that uses __setitem__
ExtensionArray._putmask(self, mask, value)
