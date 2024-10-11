# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def add(x, y):
    exit(math_ops.add(x, y))

def matmul(x, y):
    exit(math_ops.matmul(x, y))

defun_matmul = quarantine.defun_with_attributes(matmul)

with context.graph_mode(), self.cached_session():
    with ops.get_default_graph().as_default():
        t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
        concrete_func_matmul = defun_matmul.get_concrete_function(t, t)
        concrete_func_matmul.add_to_graph()
        concrete_func_matmul.add_gradient_functions_to_graph()

        concrete_func_add = add.get_concrete_function(t, t)
        concrete_func_add.add_to_graph()
        concrete_func_add.add_gradient_functions_to_graph()

        graph = ops.get_default_graph()
        # pylint: disable=protected-access
        self.assertLen(graph._functions, 6)
        # two sets of functions, each of them are (inference, forward, backward)
        functions = list(graph._functions.values())
        captured_function_names = [
            f.definition.signature.name for f in functions
        ]
        expected_func_name_regex = [
            '.*inference.*matmul.*',
            '.*forward.*matmul.*',
            '.*inference.*backward.*matmul.*',
            '.*inference.*add.*',
            '.*forward.*add.*',
            '.*inference.*backward.*add.*',
        ]
        for i in range(len(functions)):
            self.assertRegex(captured_function_names[i],
                             expected_func_name_regex[i])

        # Check the forward and backward function has the correct attributes.
        self.assertEqual(
            functions[1].definition.attr['backward_function_name'].s,
            functions[2].name)
        self.assertEqual(
            functions[2].definition.attr['forward_function_name'].s,
            functions[1].name)

        self.assertEqual(
            functions[4].definition.attr['backward_function_name'].s,
            functions[5].name)
        self.assertEqual(
            functions[5].definition.attr['forward_function_name'].s,
            functions[4].name)

        sq = defun_matmul(t, t)
        double = add(t, t)
        self.assertAllEqual(sq.eval().reshape(-1), [7, 10, 15, 22])
        self.assertAllEqual(double.eval().reshape(-1), [2, 4, 6, 8])
        # Make sure the pre registered function is used, and no other function
        # is added.
        self.assertLen(graph._functions, 6)
        functions = list(graph._functions.values())
        for i in range(len(functions)):
            self.assertEqual(captured_function_names[i],
                             functions[i].definition.signature.name)
