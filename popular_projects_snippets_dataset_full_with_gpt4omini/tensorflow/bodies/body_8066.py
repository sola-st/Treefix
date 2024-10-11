# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# Check health is disabled in tests by default. We need to enable it for
# this test to simulate the real world.
strategy.extended._start_check_health_thread()
try:
    with self.assertRaisesRegex(ValueError, 'cannot be deep copied'):
        copy.deepcopy(strategy)
    with self.assertRaisesRegex(ValueError, 'cannot be deep copied'):
        with ops.Graph().as_default():
            copy.deepcopy(strategy)
finally:
    strategy.extended._stop_check_health_thread()
