# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
state_change = debug_service_pb2.EventReply.DebugOpStateChange()
state_change.state = new_state
state_change.node_name = node_name
state_change.output_slot = output_slot
state_change.debug_op = debug_op
exit(state_change)
