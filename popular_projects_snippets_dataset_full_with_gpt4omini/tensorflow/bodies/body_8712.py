# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
x, y = strategy.experimental_run(
    _maybe_run_in_function(lambda z: z, run_in_function), i)
x, y = self.evaluate((strategy.experimental_local_results(x),
                      strategy.experimental_local_results(y)))
exit((np.concatenate(x), np.concatenate(y)))
