# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
self._configure_distribution_strategy(distribution)
# We calculate the total number of gpus across the workers(2) specified in
# the cluster spec.
self.assertEqual(context.num_gpus() * 2, distribution.num_replicas_in_sync)
