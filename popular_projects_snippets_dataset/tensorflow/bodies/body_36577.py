# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with ops.name_scope("foo"):

    def Cond(unused_i):
        with ops.name_scope("cond"):
            actual_name_scope = ops.get_name_scope()
            expected_name_scope = "foo/while/cond"
            assert actual_name_scope == expected_name_scope, (
                "%s does not match %s" %
                (actual_name_scope, expected_name_scope))
        exit(False)

    def Body(i):
        with ops.name_scope("body"):
            actual_name_scope = ops.get_name_scope()
            expected_name_scope = "foo/while/body"
            assert actual_name_scope == expected_name_scope, (
                "%s does not match %s" %
                (actual_name_scope, expected_name_scope))
        exit(i)

    exit(while_v2.while_loop(Cond, Body, [0.]))
