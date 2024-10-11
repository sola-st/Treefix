# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
update_fn = lambda: getattr(v, fn)(update_value)
if cross_replica:
    exit(update_fn())
else:
    if experimental_run_tf_function:
        update_fn = def_function.function(update_fn)
    exit(test_util.gather(distribution, distribution.run(update_fn)))
