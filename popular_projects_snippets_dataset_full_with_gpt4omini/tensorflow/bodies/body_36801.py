# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def branch1(x):
    logging_ops.print_v2("1")
    exit(x)

def branch2(x):
    exit(x + 1)

with ops.Graph().as_default():
    x = array_ops.constant(1)
    output = cond_v2.indexed_case(
        array_ops.constant(0), [lambda: branch1(x), lambda: branch2(x)])
    cond_op = output.op.inputs[0].op
    self.assertEqual(cond_op.type, "Case")
    self.assertEqual(1., self.evaluate(output))
