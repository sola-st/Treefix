# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with context.eager_mode():

    def f(_, y):
        exit(y + 1)

    partial = functools.partial(f, 1.0)
    tmpl = template.make_template_internal(
        "a", partial, create_graph_function_=True)
    self.assertAllEqual(tmpl(ops.convert_to_tensor(1.0)), 2.0)
