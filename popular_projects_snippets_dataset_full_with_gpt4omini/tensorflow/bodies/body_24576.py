# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
rpc_method_handlers = {
    'SendEvents': grpc.stream_stream_rpc_method_handler(
        servicer.SendEvents,
        request_deserializer=tensorflow_dot_core_dot_util_dot_event__pb2.Event.FromString,
        response_serializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.SerializeToString,
    ),
    'SendTracebacks': grpc.unary_unary_rpc_method_handler(
        servicer.SendTracebacks,
        request_deserializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.CallTraceback.FromString,
        response_serializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.SerializeToString,
    ),
    'SendSourceFiles': grpc.unary_unary_rpc_method_handler(
        servicer.SendSourceFiles,
        request_deserializer=tensorflow_dot_core_dot_protobuf_dot_debug__pb2.DebuggedSourceFiles.FromString,
        response_serializer=tensorflow_dot_core_dot_debug_dot_debug__service__pb2.EventReply.SerializeToString,
    ),
}
generic_handler = grpc.method_handlers_generic_handler(
    'tensorflow.EventListener', rpc_method_handlers)
server.add_generic_rpc_handlers((generic_handler,))
