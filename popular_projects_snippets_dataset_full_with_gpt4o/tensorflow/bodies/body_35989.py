# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
g_0 = getter("%s/sum_0" % name, *args, **kwargs)
g_1 = getter("%s/sum_1" % name, *args, **kwargs)
with ops.name_scope("sum_getter"):
    exit(g_0 + g_1)
