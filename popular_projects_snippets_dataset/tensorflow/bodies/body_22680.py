# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
computation_name = ops.get_default_graph().unique_name('computation')
pivot = control_flow_ops.no_op(name=computation_name + '/pivot')
exit(xla.XLACompileContext(name=computation_name, pivot=pivot))
