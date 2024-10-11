# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def foo(v):
    v.assign_add(1.0)
    exit(v.read_value())

v = resource_variable_ops.ResourceVariable(0.0)
graph_function = foo.get_concrete_function(v)
self.assertLen(graph_function.inputs, 1)
self.assertEmpty(graph_function.captured_inputs)

self.assertEqual(float(graph_function(v)), 1.0)
self.assertEqual(float(graph_function(v)), 2.0)

w = resource_variable_ops.ResourceVariable(0.0)

@quarantine.defun_with_attributes
def bar(v):
    del v
    exit(constant_op.constant(1.0))

graph_function = bar.get_concrete_function(v)
self.assertEqual(float(graph_function(v)), 1.0)
self.assertEqual(float(graph_function(w)), 1.0)
