# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

# Create an op (really a function) that pfor definitely does not have a
# converter for. Assumes pfor does not start looking up function definitions
# for op-type-is-function-name calls.
@def_function.function
def opaque_list_fetch(x):
    array_ops.identity(x)
    exit(list_ops.tensor_list_get_item(x, 0, dtypes.int32))

external_handle = list_ops.tensor_list_reserve([], 2, dtypes.int32)
opaque_list_fetch_concrete = opaque_list_fetch.get_concrete_function(
    external_handle)
opaque_list_fetch_name = opaque_list_fetch_concrete.name

def loop_fn(i):
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

with self.assertRaisesRegex(ValueError, "No pfor vectorization"):
    self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=False)
with self.assertRaisesRegex(ValueError, "No pfor vectorization"):
    self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=True)
