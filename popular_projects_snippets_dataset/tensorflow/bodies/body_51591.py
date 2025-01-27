# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = module.Module()
root.v1 = variables.Variable(1.0)
root.v2 = variables.Variable(2.0)
root.v3 = variables.Variable(3.0)
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)
restore_count = 0

def _count_restores(op_type, *unused_args, **unused_kwargs):
    nonlocal restore_count
    if op_type == b"RestoreV2":
        restore_count += 1

op_callbacks.add_op_callback(_count_restores)
save.save(root, path)
test_load(path, use_cpp_bindings=use_cpp_bindings)
op_callbacks.remove_op_callback(_count_restores)
self.assertEqual(1, restore_count)
