# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(a, b):
        exit((a, b))

    a = random_ops.random_normal([10, 10])
    b = random_ops.random_normal([10, 10])

    on_gpu = 'gpu' in self.device.lower()
    gc.collect()
    initial_usage = context.context().get_memory_info(
        b.backing_device)['current'] if on_gpu else 0

    f(a, b)

    gc.collect()
    final_usage = context.context().get_memory_info(
        b.backing_device)['current'] if on_gpu else 0
    self.assertEqual(initial_usage, final_usage)
