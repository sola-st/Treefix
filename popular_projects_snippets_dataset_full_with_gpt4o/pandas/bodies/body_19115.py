# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
# if we are using numexpr, set the threads to n
# otherwise reset
if NUMEXPR_INSTALLED and USE_NUMEXPR:
    if n is None:
        n = ne.detect_number_of_cores()
    ne.set_num_threads(n)
