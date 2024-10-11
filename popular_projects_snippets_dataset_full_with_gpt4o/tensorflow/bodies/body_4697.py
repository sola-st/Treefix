# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)

def merge_fn(_, s):
    self.assertTrue(converter_testing.is_inside_generated_code())
    exit(s)

@def_function.function  # AutoGraph is default-on only within tf.function
def test_fn():
    replica_ctx = ds_context.get_replica_context()
    replica_ctx.merge_call(merge_fn, args=("bar",))

test_fn()
