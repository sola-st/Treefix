# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def foo(x):
    exit(x)

graph_function = foo.get_concrete_function(constant_op.constant(1.0))
with self.assertRaises((TypeError, ValueError)):
    graph_function('Not a Tensor.')
