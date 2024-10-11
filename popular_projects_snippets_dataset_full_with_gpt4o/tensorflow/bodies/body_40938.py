# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    on_gpu = 'gpu' in self.device.lower()
    v = variables.Variable([3.1, 3.2])

    @polymorphic_function.function(jit_compile=True)
    def update_var(a, b):
        v.assign_add(a * b)

    arg1 = random_ops.random_normal([2])
    arg2 = random_ops.random_normal([2])

    gc.collect()
    initial_usage = context.context().get_memory_info(
        v.device)['current'] if on_gpu else 0
    update_var(arg1, arg2)
    gc.collect()
    final_usage = context.context().get_memory_info(
        v.device)['current'] if on_gpu else 0
    self.assertEqual(initial_usage, final_usage)
