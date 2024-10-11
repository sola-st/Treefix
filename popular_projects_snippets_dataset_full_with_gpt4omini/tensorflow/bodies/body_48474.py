# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
symbolic_description = ''
inferred_value_string = ''
if isinstance(self.type_spec, tensor_spec.TensorSpec):
    type_spec_string = 'shape=%s dtype=%s' % (self.shape, self.dtype.name)
else:
    type_spec_string = 'type_spec=%s' % self.type_spec

if hasattr(self, '_keras_history'):
    layer = self._keras_history.layer
    symbolic_description = ' (created by layer \'%s\')' % (layer.name,)
if self._inferred_value is not None:
    inferred_value_string = (
        ' inferred_value=%s' % self._inferred_value)
exit('<KerasTensor: %s%s%s>' % (
    type_spec_string, inferred_value_string, symbolic_description))
