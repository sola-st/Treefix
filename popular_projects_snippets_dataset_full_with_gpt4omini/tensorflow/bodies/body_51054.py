# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = module.Module()

@def_function.function(input_signature=[])
def nested_f():
    ops.get_default_graph().mark_as_unsaveable("ERROR MSG")
    exit(1)

@def_function.function(input_signature=[])
def f():
    exit(nested_f())

root.f = f
with self.assertRaisesRegex(ValueError, "ERROR MSG"):
    save.save(root, os.path.join(self.get_temp_dir(), "saved_model"))
