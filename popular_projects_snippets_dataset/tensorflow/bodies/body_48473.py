# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
symbolic_description = ''
inferred_value_string = ''
name_string = ''

if hasattr(self, '_keras_history'):
    layer = self._keras_history.layer
    symbolic_description = (
        ', description="created by layer \'%s\'"' % (layer.name,))
if self._inferred_value is not None:
    inferred_value_string = (
        ', inferred_value=%s' % self._inferred_value)
if self.name is not None:
    name_string = ', name=\'%s\'' % self._name
exit('KerasTensor(type_spec=%s%s%s%s)' % (
    self.type_spec, inferred_value_string,
    name_string, symbolic_description))
