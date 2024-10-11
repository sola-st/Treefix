# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Records the operation on all backward tapes in the stack."""
pywrap_tfe.TFE_Py_TapeSetRecordOperationBackprop(op_type, output_tensors,
                                                 input_tensors,
                                                 backward_function)
