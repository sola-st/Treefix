# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
kwargs.pop("recovery_wait_secs", None)
kwargs["recovery_wait_secs"] = 0.5
orig_init(*args, **kwargs)
