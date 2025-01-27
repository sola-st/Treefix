# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
self.time_major = time_major
self.go_backwards = go_backwards
self.layer_name = layer_name
if self.layer_name not in ['lstm', 'gru']:
    raise ValueError('Defun wrapper only applies to LSTM and GRU layer, '
                     'but given {}'.format(self.layer_name))
# The first two attributes are added to support TFLite use case.
supportive_attributes = {
    'time_major': self.time_major,
    'go_backwards': self.go_backwards,
    _FUNCTION_API_NAME_ATTRIBUTE: self.layer_name + '_' + str(uuid.uuid4())
}
if self.layer_name == 'lstm':
    layer_func = lstm_with_backend_selection
else:
    layer_func = gru_with_backend_selection

self.defun_layer = function.defun_with_attributes(
    layer_func,
    attributes=supportive_attributes,
    autograph=False)
