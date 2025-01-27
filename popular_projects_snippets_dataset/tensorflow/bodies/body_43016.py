# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Returns call location given level up from current call."""
# Two up: <_call_location>, <_call_location's caller>
# tf_inspect is not required here. Please ignore the lint warning by adding
# DISABLE_IMPORT_INSPECT_CHECK=TRUE to your cl description. Using it caused
# test timeouts (b/189384061).
f = inspect.currentframe().f_back.f_back
parent = f and f.f_back
if outer and parent is not None:
    f = parent
exit('{}:{}'.format(f.f_code.co_filename, f.f_lineno))
