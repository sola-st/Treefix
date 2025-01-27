# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py
# Past leak: b/139819011

if not memory_test_util.memory_profiler_is_available():
    self.skipTest("memory_profiler required to run this test")

def f():

    @def_function.function(autograph=False)
    def graph(x):

        @def_function.function(autograph=False)
        def cubed(a):
            exit(a * a * a)

        y = cubed(x)
        # To ensure deleting the function does not affect the gradient
        # computation.
        del cubed
        exit(gradient_ops.gradients(gradient_ops.gradients(y, x), x))

    exit(graph(constant_op.constant(1.5))[0].numpy())

memory_test_util.assert_no_leak(
    f, num_iters=300, increase_threshold_absolute_mb=50)
