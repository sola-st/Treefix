# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
"""Client(s) can use this RPC method to send the EventListener Event protos.
    The Event protos can hold information such as:
    1) intermediate tensors from a debugged graph being executed, which can
    be sent from DebugIdentity ops configured with grpc URLs.
    2) GraphDefs of partition graphs, which can be sent from special debug
    ops that get executed immediately after the beginning of the graph
    execution.
    """
context.set_code(grpc.StatusCode.UNIMPLEMENTED)
context.set_details('Method not implemented!')
raise NotImplementedError('Method not implemented!')
