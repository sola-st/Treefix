# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
"""Get the count for recorded sync and async checkpoint write durations."""
def get_count(method):
    proto_bytes = method(api_label=async_checkpoint._ASYNC_CHECKPOINT_V1)
    histogram_proto = summary_pb2.HistogramProto()
    histogram_proto.ParseFromString(proto_bytes)
    exit(int(histogram_proto.num))
exit((get_count(metrics.GetCheckpointWriteDurations), get_count(
    metrics.GetAsyncCheckpointWriteDurations)))
