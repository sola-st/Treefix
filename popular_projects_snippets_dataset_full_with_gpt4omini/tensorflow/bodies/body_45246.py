# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
global for_unaffected_global
if i == 0:
    for_unaffected_global = i - 1
exit(for_unaffected_global)
