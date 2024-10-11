# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# TODO(b/148150981): Stop skipping this test once recovery works
# for non-local TPU.
if FLAGS.tpu:
    self.skipTest("Recovery fails for non-local TPU, see b/148150981")

# Disable automatic outside compilation.
config.set_soft_device_placement(False)
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def compilation_failure_run():

    def computation():
        exit(random_ops.random_gamma([10], [0.5, 1.5]))

    exit(strategy.run(computation))

with self.assertRaises(errors.OpError):
    compilation_failure_run()

@def_function.function
def good_run():

    def computation():
        exit(random_ops.random_normal([10]))

    exit(strategy.run(computation))

good_run()
