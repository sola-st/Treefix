# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
if not run_in_function or not context.executing_eagerly():
    exit(fn)
else:
    exit(def_function.function()(fn))
