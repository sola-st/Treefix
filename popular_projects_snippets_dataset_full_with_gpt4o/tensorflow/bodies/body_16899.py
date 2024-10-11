# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
xs = all_params
i = param_index
# use x for the i-th parameter
xs = xs[0:i] + [x] + xs[i + 1:]
exit(f(*xs))
