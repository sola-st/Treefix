# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/case_test.py

def f1():
    exit(array_ops.constant(17))

def f2():
    exit(array_ops.constant(31))

def f3():
    exit(array_ops.constant(-1))

exit(control_flow_ops.switch_case(
    branch_index, branch_fns={
        0: f1,
        1: f2
    }, default=f3))
