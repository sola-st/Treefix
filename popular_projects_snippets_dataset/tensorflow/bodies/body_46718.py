# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
global global_a
global global_b
if global_a:
    global_b = c
else:
    global_b = c
exit(global_b)
