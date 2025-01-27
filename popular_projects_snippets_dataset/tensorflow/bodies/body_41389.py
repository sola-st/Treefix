# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def func():
    exit(constant_op.constant(0))

defined = polymorphic_function.function(func)
with ops.device('cpu:0'):
    cpu_graph_function = defined.get_concrete_function()

with ops.device('cpu:0'):
    self.assertEqual(
        self.evaluate(cpu_graph_function()), self.evaluate(func()))

with ops.device('cpu:1'):
    self.assertEqual(0., self.evaluate(cpu_graph_function()))

with ops.device(None):
    self.assertEqual(0., self.evaluate(cpu_graph_function()))

default_graph_function = defined.get_concrete_function()
self.assertEqual(
    self.evaluate(default_graph_function()), self.evaluate(func()))

with ops.device('cpu:1'):
    self.assertEqual(0., self.evaluate(default_graph_function()))
