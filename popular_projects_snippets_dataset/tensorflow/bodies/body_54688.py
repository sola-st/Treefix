# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op_test.py

@def_function.function
def f_using_eagerconst():
    x = constant_op.constant(1.)
    graph_def = self._make_graph_def("""
         node { name: 'x' op: 'Placeholder'
                attr { key: 'dtype' value { type: DT_FLOAT } }}
         node { name: 'const' op: '_EagerConst' input: 'x:0'
                attr { key: 'T' value { type: DT_FLOAT } }}""")
    x_id = importer.import_graph_def(
        graph_def,
        input_map={"x:0": x},
        return_elements=["const"],
        name="import")[0].outputs[0]
    gradients_impl.gradients(x_id, x)
    exit(x_id)

with self.assertRaisesRegex(AssertionError, "Please file a bug"):
    f_using_eagerconst()
