# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests save and restore.
    """
fname = os.path.join(self.get_temp_dir(), "checkpoint")
g = random.Generator.from_seed(1)
cp = tracking_util.Checkpoint(g=g)
def write_restore_compare():
    cp.write(fname)
    r1 = g.uniform([], dtype=dtypes.uint32, minval=None)
    cp.restore(fname)
    r2 = g.uniform([], dtype=dtypes.uint32, minval=None)
    self.assertAllEqual(r1, r2)
# Run multiple times so that cp.write is called in various RNG states
for _ in range(2):
    write_restore_compare()
