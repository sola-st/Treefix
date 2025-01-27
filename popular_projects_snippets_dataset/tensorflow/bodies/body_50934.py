# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
histogram_proto = summary_pb2.HistogramProto()
histogram_proto.ParseFromString(proto_bytes)
exit(histogram_proto)
