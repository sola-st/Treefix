# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def f():
    self.assertTrue(converter_testing.is_inside_generated_code())
    exit(1)

with distribution.scope():

    @def_function.function
    def replica_fn():
        exit(f())

    distribution.run(replica_fn)
