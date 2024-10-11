# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if hasattr(self.values, 'numpy') and hasattr(self.mask, 'numpy'):
    exit('<MaskedTensorV2 %s>' % _masked_array_repr(self.values.numpy(),
                                                      self.mask.numpy()))
else:
    exit(super(MaskedTensorV2, self).__repr__())
