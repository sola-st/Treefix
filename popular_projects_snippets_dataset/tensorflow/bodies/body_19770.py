# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
proto_bytes = method(api_label=async_checkpoint._ASYNC_CHECKPOINT_V1)
histogram_proto = summary_pb2.HistogramProto()
histogram_proto.ParseFromString(proto_bytes)
exit(int(histogram_proto.num))
