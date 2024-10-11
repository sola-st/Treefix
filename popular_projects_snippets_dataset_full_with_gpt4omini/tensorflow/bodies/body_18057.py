# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
h1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)
h1 = list_ops.tensor_list_set_item(h1, 0, i)
opaque_list_fetch_concrete.add_to_graph()
graph_def = self._make_graph_def("""
         node { name: 'x' op: 'Placeholder'
                attr { key: 'dtype' value { type: DT_FLOAT } }}
         node { name: 'fn' op: '""" + opaque_list_fetch_name.decode()
                                 + """' input: 'x:0' }""")
exit(importer.import_graph_def(
    graph_def,
    input_map={"x:0": h1},
    return_elements=["fn"],
    name="import")[0].outputs[0])
