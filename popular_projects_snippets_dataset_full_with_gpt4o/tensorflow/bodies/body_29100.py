# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
pb = dataset_options_pb2.Options()
options = options_lib.Options()
options._from_proto(pb)
result = options._to_proto()
expected_pb = dataset_options_pb2.Options()
expected_pb.autotune_options.CopyFrom(dataset_options_pb2.AutotuneOptions())
expected_pb.distribute_options.CopyFrom(
    dataset_options_pb2.DistributeOptions())
expected_pb.optimization_options.CopyFrom(
    dataset_options_pb2.OptimizationOptions())
expected_pb.threading_options.CopyFrom(
    dataset_options_pb2.ThreadingOptions())
self.assertProtoEquals(expected_pb, result)
