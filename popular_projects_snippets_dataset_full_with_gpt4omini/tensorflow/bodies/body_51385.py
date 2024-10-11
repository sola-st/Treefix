# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
# Tests that signatures saved using TF1 can be resaved with TF2.
# See b/211666001 for context.
export_graph = ops.Graph()
with export_graph.as_default():
    a = array_ops.placeholder(
        shape=[None, 1], dtype=dtypes.float32, name="input_2")
    b = array_ops.placeholder(
        shape=[None, 2], dtype=dtypes.float32, name="input_1")
    c = array_ops.identity(a)
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"a": a, "b": b},
            outputs={"c": c})
imported = load.load(path)
path2 = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
save.save(imported, path2, imported.signatures)

imported2 = load.load(path2)
self.assertEqual(
    imported2.signatures["serving_default"](
        a=constant_op.constant([5.]),
        b=constant_op.constant([1., 3.]))["c"].numpy(), 5.)
