# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
"""Constructor.

    Args:
      channel: A grpc.Channel.
    """
self.SendEvents = channel.stream_stream(
    '/tensorflow.EventListener/SendEvents',
    request_serializer=tensorflow_dot_core_dot_util_dot_event__pb2.Event.SerializeToString,
    response_deserializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.FromString,
    )
self.SendTracebacks = channel.unary_unary(
    '/tensorflow.EventListener/SendTracebacks',
    request_serializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.CallTraceback.SerializeToString,
    response_deserializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.FromString,
    )
self.SendSourceFiles = channel.unary_unary(
    '/tensorflow.EventListener/SendSourceFiles',
    request_serializer=tensorflow_dot_core_dot_protobuf_dot_debug__pb2.DebuggedSourceFiles.SerializeToString,
    response_deserializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.FromString,
    )
