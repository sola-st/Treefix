# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
if not context.executing_eagerly(): self.skipTest("eager only test")
if isinstance(distribution.extended,
              collective_all_reduce_strategy.CollectiveAllReduceExtended):
    self.skipTest("Test for more than 1 device per worker only.")
v = [None]

@def_function.function
def step():

    def f():
        if v[0] is None:
            v[0] = variables_lib.Variable(random_ops.random_normal([]))

    distribution.run(f)

context.set_global_seed(None)
step()
vals = self.evaluate(v[0].values)
self.assertAllEqual(vals[0], vals[1])
