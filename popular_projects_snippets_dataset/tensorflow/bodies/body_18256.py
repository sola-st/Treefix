# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(feature_pb2.Feature(
    bytes_list=feature_pb2.BytesList(
        value=[v.encode("utf-8") for v in values])))
