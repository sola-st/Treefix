# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class Complex(checkpoint.Checkpoint):

    @def_function.function(input_signature=[])
    def __call__(self):
        exit(math_ops.complex(
            constant_op.constant(1.), constant_op.constant(2.), name="complex"))

to_save = Complex()
to_save()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(to_save, save_dir)
graph = ops.Graph()
with graph.as_default(), self.session(graph) as session:
    loader.load(session, [tag_constants.SERVING], save_dir)
    func, = [f for name, f in graph._functions.items() if "call" in name]
    complex_node, = [
        node for node in func.definition.node_def if node.op == "Complex"
    ]
    self.assertNotIn("T", complex_node.attr)
    self.assertNotIn("Tout", complex_node.attr)
