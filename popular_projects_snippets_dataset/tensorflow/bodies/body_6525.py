# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
if not context.executing_eagerly():
    self.skipTest("`tf.function` is an eager-only feature")

v = [None]

def model_fn():
    if v[0] is None:
        init_val = array_ops.zeros([])
        v[0] = variables.Variable(init_val)
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v[0])

@def_function.function(autograph=False, jit_compile=True)
def make_v1():
    exit(distribution.experimental_local_results(
        distribution.extended.call_for_each_replica(model_fn)))

with self.assertRaisesRegex(
    errors.UnimplementedError,
    "We failed to lift variable creations out of this tf.function, "
    "so this tf.function cannot be run on XLA."):
    _ = make_v1()
