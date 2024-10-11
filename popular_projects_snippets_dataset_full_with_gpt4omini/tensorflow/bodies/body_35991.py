# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def sum_getter(getter, name, *args, **kwargs):
    g_0 = getter("%s/sum_0" % name, *args, **kwargs)
    g_1 = getter("%s/sum_1" % name, *args, **kwargs)
    with ops.name_scope("sum_getter"):
        exit(g_0 + g_1)

def prod_getter(getter, name, *args, **kwargs):
    g_0 = getter("%s/prod_0" % name, *args, **kwargs)
    g_1 = getter("%s/prod_1" % name, *args, **kwargs)
    with ops.name_scope("prod_getter"):
        exit(g_0 * g_1)

with variable_scope.variable_scope("prod_scope", custom_getter=prod_getter):
    with variable_scope.variable_scope("sum_scope", custom_getter=sum_getter):
        with variable_scope.variable_scope(
            "inner_sum_scope", custom_getter=sum_getter):
            # take sums of sums of products
            v = variable_scope.get_variable("v", [1, 2, 3])

self.assertEqual([1, 2, 3], v.get_shape())
true_vars = variables_lib.trainable_variables()
self.assertEqual(8, len(true_vars))
template = (
    "prod_scope/sum_scope/inner_sum_scope/v/sum_%d/sum_%d/prod_%d:0")
self.assertEqual(template % (0, 0, 0), true_vars[0].name)
self.assertEqual(template % (0, 0, 1), true_vars[1].name)
self.assertEqual(template % (0, 1, 0), true_vars[2].name)
self.assertEqual(template % (0, 1, 1), true_vars[3].name)
self.assertEqual(template % (1, 0, 0), true_vars[4].name)
self.assertEqual(template % (1, 0, 1), true_vars[5].name)
self.assertEqual(template % (1, 1, 0), true_vars[6].name)
self.assertEqual(template % (1, 1, 1), true_vars[7].name)

with self.cached_session() as sess:
    variables_lib.global_variables_initializer().run()
    np_vars, np_v = self.evaluate([true_vars, v])
    # take products of sums of products
    self.assertAllClose(
        np_v, (((np_vars[0] * np_vars[1]) + (np_vars[2] * np_vars[3])) + (
            (np_vars[4] * np_vars[5]) + (np_vars[6] * np_vars[7]))))
