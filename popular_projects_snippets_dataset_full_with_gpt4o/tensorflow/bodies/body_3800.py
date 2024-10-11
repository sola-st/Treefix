# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

def g():
    exit(x + 1)

exit(g())
