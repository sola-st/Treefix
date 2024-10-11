# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = variables.Variable(1.0)

def trivial_function():
    exit(control_flow_ops.cond(
        array_ops.placeholder_with_default(True, ()), v.read_value,
        v.read_value))

graph_function = tracing_compiler.TracingCompiler(
    trivial_function, 'test', capture_by_value=True)

self.assertAllEqual(graph_function(), 1.0)
v.assign(2.0)
self.assertAllEqual(graph_function(), 1.0)
