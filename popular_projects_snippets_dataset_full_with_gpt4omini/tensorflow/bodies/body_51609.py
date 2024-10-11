# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
model = module.Module()
model.mapping = lookup_ops.StaticHashTable(
    lookup_ops.KeyValueTensorInitializer(
        keys=math_ops.range(1, dtype=dtypes.int32), values=["foo"]
    ),
    "default_value",
)
loaded = cycle(model, 1, use_cpp_bindings=use_cpp_bindings)
del model
del loaded
# Exceptions raised during garbage collection are simply printed to stderr
# and ignored, and we have no way to access them. We'll capture stdout
# during the garbage collection process and inspect to see if any
# exceptions were raised.
stderr = io.StringIO()
with contextlib.redirect_stderr(stderr):
    gc.collect()
if "Exception ignored in" in stderr.getvalue():
    raise Exception(stderr.getvalue())
