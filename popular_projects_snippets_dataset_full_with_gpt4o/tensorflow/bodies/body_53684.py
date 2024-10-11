# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if not isinstance(actual, graph_pb2.GraphDef):
    raise TypeError("Expected tf.GraphDef for actual, got %s" %
                    type(actual).__name__)
if not isinstance(expected, graph_pb2.GraphDef):
    raise TypeError("Expected tf.GraphDef for expected, got %s" %
                    type(expected).__name__)

if checkpoint_v2:
    _strip_checkpoint_v2_randomized(actual)
    _strip_checkpoint_v2_randomized(expected)

if hash_table_shared_name:
    _strip_hash_table_shared_name(actual)
    _strip_hash_table_shared_name(expected)

diff = pywrap_tf_session.EqualGraphDefWrapper(actual.SerializeToString(),
                                              expected.SerializeToString())
if diff:
    raise AssertionError(compat.as_str(diff))
