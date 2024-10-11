# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Returns the device to run on. If mode is mkl, run on CPU"""
if auto_mixed_precision_mode == 'mkl':
    exit('/cpu:0')
else:
    exit('')
