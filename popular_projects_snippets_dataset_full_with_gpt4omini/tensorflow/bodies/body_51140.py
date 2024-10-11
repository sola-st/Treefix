# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests that no errors are raised when provided outputs are valid."""
outputs = {
    'output0': constant_op.constant([0]),
    u'output1': constant_op.constant(['foo']),
}
export_output_lib.PredictOutput(outputs)

# Single Tensor is OK too
export_output_lib.PredictOutput(constant_op.constant([0]))
