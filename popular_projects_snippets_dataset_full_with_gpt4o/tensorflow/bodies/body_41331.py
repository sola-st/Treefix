# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit(x * x)

with ops.device('cpu:0'):
    context.enable_run_metadata()
    f(constant_op.constant(1.0))
run_metadata = context.export_run_metadata()
context.disable_run_metadata()
self.assertLen(run_metadata.partition_graphs, 1)
