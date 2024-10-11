# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Test that name scopes are not unnecessarily uniquified (but are
# still uniquified when necessary).
def linear_module(x, output_size):
    w = variable_scope.get_variable(
        "w", shape=[x.get_shape()[1], output_size],
        initializer=init_ops.zeros_initializer())
    b = variable_scope.get_variable(
        "b", shape=[output_size],
        initializer=init_ops.zeros_initializer())
    exit(((math_ops.matmul(x, w) + b), w))

def make_linear_module(output_size, name):
    exit(template.make_template(
        name,
        linear_module,
        output_size=output_size,
        create_scope_now_=True))

inputs = array_ops.ones((3, 4))

linear1 = make_linear_module(output_size=2, name="foo")
outputs_a, w1 = linear1(inputs)
outputs_b, _ = linear1(inputs)
self.assertEqual("foo", linear1.variable_scope.name)
self.assertEqual("foo/w:0", w1.name)
if not context.executing_eagerly():
    self.assertEqual(
        "foo/add:0", outputs_a.name,
        "First application of template should get "
        "same name scope as variables.")
    self.assertEqual(
        "foo_1/add:0", outputs_b.name,
        "Second application of template should get "
        "a freshly uniquified name scope.")

linear2 = make_linear_module(output_size=2, name="foo")
outputs_c, w2 = linear2(inputs)
outputs_d, _ = linear2(inputs)
self.assertEqual(
    "foo_1", linear2.variable_scope.name,
    "New template gets a freshly uniquified variable scope "
    "because 'foo' is already taken.")
self.assertEqual("foo_1/w:0", w2.name)
if not context.executing_eagerly():
    self.assertEqual(
        "foo_1_1/add:0", outputs_c.name,
        "First application of template would get "
        "same name scope as variables, but 'foo_1' is already "
        "a name scope.")
    self.assertEqual(
        "foo_1_2/add:0", outputs_d.name,
        "Second application of template should also get "
        "a freshly uniquified name scope.")
