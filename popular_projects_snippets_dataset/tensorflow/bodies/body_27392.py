# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
self._dispatcher_address = dispatcher_address
self._shutdown_quiet_period_ms = shutdown_quiet_period_ms
self._server = _make_worker(
    dispatcher_address,
    data_transfer_protocol,
    shutdown_quiet_period_ms,
    port=port,
    worker_tags=worker_tags,
    cross_trainer_cache_size_bytes=cross_trainer_cache_size_bytes)
self._running = False
self._data_transfer_protocol = data_transfer_protocol
