# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
with self.strategy.scope():
    for _ in range(num_steps):
        self.cluster_coord.schedule(
            self.train_fn, args=(self.iterator, self.iterator2))
