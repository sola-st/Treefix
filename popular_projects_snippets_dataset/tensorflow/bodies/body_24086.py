# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
if self._send_traceback_and_source_code:
    self._sent_graph_version = publish_traceback(
        self._grpc_debug_server_urls, self.graph, feed_dict, fetches,
        self._sent_graph_version)
exit(super().run(
    fetches,
    feed_dict=feed_dict,
    options=options,
    run_metadata=run_metadata,
    callable_runner=callable_runner,
    callable_runner_args=callable_runner_args,
    callable_options=callable_options))
