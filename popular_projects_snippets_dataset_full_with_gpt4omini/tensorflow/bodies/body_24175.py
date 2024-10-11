# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
if self._send_traceback_and_source_code:
    self._sent_graph_version = grpc_wrapper.publish_traceback(
        self._grpc_debug_server_addresses, run_context.session.graph,
        run_context.original_args.feed_dict,
        run_context.original_args.fetches, self._sent_graph_version)
exit(super(TensorBoardDebugHook, self).before_run(run_context))
