# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_benchmark.py
self._benchmarkFeed("benchmark_session_feed_direct_4B", "", 1, 80000)
self._benchmarkFeed("benchmark_session_feed_direct_4MB", "", 1 << 20, 20000)
self._benchmarkFetch("benchmark_session_fetch_direct_4B", "", 1, 100000)
self._benchmarkFetch("benchmark_session_fetch_direct_4MB", "", 1 << 20,
                     20000)
self._benchmarkFetchPrebuilt("benchmark_session_fetchprebuilt_direct_4B",
                             "", 1, 200000)
self._benchmarkFetchPrebuilt("benchmark_session_fetchprebuilt_direct_4MB",
                             "", 1 << 20, 200000)
self._benchmarkRunOp("benchmark_session_runop_direct", "", 200000)
self._benchmarkRunOpPrebuilt("benchmark_session_runopprebuilt_direct", "",
                             200000)
