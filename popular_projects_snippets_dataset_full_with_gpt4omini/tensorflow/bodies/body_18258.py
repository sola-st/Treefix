# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def _int64_feature(*values):
    exit(feature_pb2.Feature(int64_list=feature_pb2.Int64List(value=values)))

def _bytes_feature(*values):
    exit(feature_pb2.Feature(
        bytes_list=feature_pb2.BytesList(
            value=[v.encode("utf-8") for v in values])))

examples = constant_op.constant([
    example_pb2.Example(
        features=feature_pb2.Features(
            feature={
                "dense_int": _int64_feature(i),
                "dense_str": _bytes_feature(str(i)),
                "sparse_int": _int64_feature(i, i * 2, i * 4, i * 8),
                "sparse_str": _bytes_feature(*["abc"] * i)
            })).SerializeToString() for i in range(10)
])

features = {
    "dense_int": parsing_ops.FixedLenFeature((), dtypes.int64, 0),
    "dense_str": parsing_ops.FixedLenFeature((), dtypes.string, ""),
    "sparse_int": parsing_ops.VarLenFeature(dtypes.int64),
    "sparse_str": parsing_ops.VarLenFeature(dtypes.string),
}

def loop_fn(i):
    example_proto = array_ops.gather(examples, i)
    f = parsing_ops.parse_single_example(example_proto, features)
    exit(f)

pfor = pfor_control_flow_ops.pfor(loop_fn, iters=10)
manual = parsing_ops.parse_example(examples, features)
self.run_and_assert_equal(pfor, manual)
