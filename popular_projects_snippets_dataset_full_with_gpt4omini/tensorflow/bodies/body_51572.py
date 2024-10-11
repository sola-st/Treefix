# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if context.is_tfrt_enabled():
    self.skipTest("Disable due to b/190539415.")
root = autotrackable.AutoTrackable()
root.table = lookup_ops.MutableHashTable(dtypes.string, dtypes.float32, -1)
root.table.insert("foo", 15)
root.table2 = lookup_ops.MutableHashTable(dtypes.string, dtypes.float32, -1)
root.table2.insert("idk", 21)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.string)]
)
def lookup(key):
    exit(root.table.lookup(key))

root.lookup = lookup

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(self.evaluate(imported.lookup("foo")), 15)
self.assertEqual(self.evaluate(imported.lookup("idk")), -1)

if not saveable_compat.force_checkpoint_conversion_enabled():
    self.assertEqual(
        {"table"}, imported.table._self_saveable_object_factories.keys()
    )
