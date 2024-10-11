# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_benchmark.py
server = server_lib.Server.create_local_server()
self._benchmarkFeed("benchmark_session_feed_grpc_4B", server.target, 1,
                    30000)
session.Session.reset(server.target)
self._benchmarkFeed("benchmark_session_feed_grpc_4MB", server.target,
                    1 << 20, 25000)
session.Session.reset(server.target)
self._benchmarkFetch("benchmark_session_fetch_grpc_4B", server.target, 1,
                     40000)
session.Session.reset(server.target)
self._benchmarkFetch("benchmark_session_fetch_grpc_4MB", server.target,
                     1 << 20, 20000)
session.Session.reset(server.target)
self._benchmarkFetchPrebuilt("benchmark_session_fetchprebuilt_grpc_4B",
                             server.target, 1, 50000)
session.Session.reset(server.target)
self._benchmarkFetchPrebuilt("benchmark_session_fetchprebuilt_grpc_4MB",
                             server.target, 1 << 20, 50000)
session.Session.reset(server.target)
self._benchmarkRunOp("benchmark_session_runop_grpc", server.target, 50000)
session.Session.reset(server.target)
self._benchmarkRunOpPrebuilt("benchmark_session_runopprebuilt_grpc",
                             server.target, 100000)
session.Session.reset(server.target)
