# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

@def_function.function
def fn_with_many_reads():

    @def_function.function
    def fn_with_many_reads_inner():

        def then_branch():
            exit(math_ops.add_n(rvars))

        def else_branch():
            exit(0.)

        exit(control_flow_ops.cond(
            constant_op.constant(True), then_branch, else_branch))

    exit(fn_with_many_reads_inner())

exit(fn_with_many_reads())
