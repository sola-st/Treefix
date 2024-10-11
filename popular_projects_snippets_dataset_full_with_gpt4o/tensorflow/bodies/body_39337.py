# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_metrics_test.py
proto_bytes = metrics.GetCheckpointReadDurations(api_label=api_label)
histogram_proto = summary_pb2.HistogramProto()
histogram_proto.ParseFromString(proto_bytes)
exit(histogram_proto)
