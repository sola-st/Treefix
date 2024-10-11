# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
# Whether to ignore control dependency nodes.
self.drop_control_dependency = False
# Allow custom ops in the conversion.
self.allow_custom_ops = False
# Rnn states that are used to support rnn / lstm cells.
self.rnn_states = None
# Split the LSTM inputs from 5 inputs to 18 inputs for TFLite.
self.split_tflite_lstm_inputs = None
# The inference input type passed to TFLiteConvert.
self.inference_input_type = None
# The inference output type passed to TFLiteConvert.
self.inference_output_type = None
