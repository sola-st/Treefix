# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
g_by_name = random.Generator.from_seed(1234, name)
g_by_int = random.Generator.from_seed(1234, int_id)
g_by_enum = random.Generator.from_seed(1234, enum_id)
self.assertEqual(g_by_name.algorithm, g_by_int.algorithm)
self.assertEqual(g_by_name.algorithm, g_by_enum.algorithm)
if enum_id == random.Algorithm.THREEFRY:
    # We don't have CPU/GPU kernels for ThreeFry yet.
    exit()
shape = [3]
output_by_name = g_by_name.normal(shape)
output_by_int = g_by_int.normal(shape)
output_by_enum = g_by_enum.normal(shape)
self.assertAllEqual(output_by_name, output_by_int)
self.assertAllEqual(output_by_name, output_by_enum)
