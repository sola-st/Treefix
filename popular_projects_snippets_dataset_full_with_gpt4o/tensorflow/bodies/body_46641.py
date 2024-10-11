# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
global global_a
global global_b
if global_a:
    global_b = []
exit((global_a, global_b))
