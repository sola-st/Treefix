# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
rvars = []
for _ in range(var_count):
    rvars.append(resource_variable_ops.ResourceVariable(1.0))

# Note: We want to benchmark the graph building time so we intentionally
# add this outer function so that the tf.function gets retraced every time.
def benchmark_fn():

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

with context.device(CPU):
    self._run(benchmark_fn, 10)
