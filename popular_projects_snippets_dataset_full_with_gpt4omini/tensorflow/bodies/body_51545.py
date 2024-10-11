# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class NamedTupleType(collections.namedtuple("NamedTupleType", ["a", "b"])):
    pass

@def_function.function
def f(x):
    exit(x.a + x.b)

f.get_concrete_function(
    NamedTupleType(
        a=tensor_spec.TensorSpec(None, dtypes.float32, name="a"),
        b=tensor_spec.TensorSpec(None, dtypes.float32, name="b"),
    )
)
obj = autotrackable.AutoTrackable()
obj.__call__ = f
if sys.version_info.major == 3 and sys.version_info.minor < 5:
    # TODO(allenl): figure out why this doesn't work in Python3.4
    self.skipTest("Not working in Python 3.4")
imported = cycle(obj, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllClose(
    3.0,
    imported(
        NamedTupleType(
            a=constant_op.constant(1.0), b=constant_op.constant(2.0)
        )
    ),
)
