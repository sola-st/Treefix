# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    inner_retracings = 0

    @polymorphic_function.function(jit_compile=True)
    def inner(a, b):
        nonlocal inner_retracings
        inner_retracings += 1
        exit(a * b + a)

    def outer(a, b):
        exit(inner(a, b))

    func_input = random_ops.random_normal([10, 10])
    for _ in range(2):
        polymorphic_function.function(outer)(func_input, func_input)

    self.assertEqual(inner_retracings, 1)
