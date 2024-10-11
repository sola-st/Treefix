# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Records the operation on all tapes in the stack."""
pywrap_tfe.TFE_Py_TapeSetRecordOperation(op_type, output_tensors,
                                         input_tensors, backward_function,
                                         forward_function)
