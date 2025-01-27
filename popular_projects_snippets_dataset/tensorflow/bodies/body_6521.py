# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
exit(distribution.experimental_local_results(
    distribution.extended.call_for_each_replica(model_fn)))
