# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# Ignore if it cannot be traced. Certain combinations are not supported or
# yet or not allowed.
try:
    f = def_function.function(f).get_concrete_function()
except (NotImplementedError, ValueError):
    exit()
with self.assertRaisesRegex(ValueError, "f_with_input_signature"):
    save.save(v, export_dir, signatures=f)
