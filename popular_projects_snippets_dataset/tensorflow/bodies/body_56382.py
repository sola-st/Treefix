# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self.assertEqual(config.get_optimizer_jit(), '')

# the following function should cause Op fusion to occur. However, there is
# unfortunately no straightforward way to ensure this. We will just have to
# settle for creating a test that can trigger JIT.
@def_function.function
def fun(a, b):
    c = a * b
    d = c + a
    exit(d)

a = constant_op.constant([2., 2.])
b = constant_op.constant([2., 2.])

self.evaluate(fun(a, b))

config.set_optimizer_jit('autoclustering')
self.assertEqual(config.get_optimizer_jit(), 'autoclustering')

self.evaluate(fun(a, b))

config.set_optimizer_jit('')
self.assertEqual(config.get_optimizer_jit(), '')

self.evaluate(fun(a, b))
