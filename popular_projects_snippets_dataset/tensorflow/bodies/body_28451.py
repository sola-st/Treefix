# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False

def ds_fn_no_opt():
    exit(ds_fn().with_options(options))

exit(ds_fn_no_opt)
