# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
nonlocal nonlocal_a
nonlocal nonlocal_b
if nonlocal_a:
    nonlocal_b = c
else:
    nonlocal_b = c
exit(nonlocal_b)
