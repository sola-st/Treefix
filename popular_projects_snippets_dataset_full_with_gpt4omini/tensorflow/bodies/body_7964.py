# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
distribute_lib.distribution_strategy_input_api_counter.get_cell(
    self.__class__.__name__, "PSSDistributedLookupTable").increase_by(1)
self._coordinator_instance = wrapped_creator()
self._wrapped_creator = wrapped_creator
self._coordinator = strategy._cluster_coordinator
# self._distributed_table is a RemoteValue mapping worker_index to
# RemoteValue that wraps a resource handle on the worker
self._distributed_table = None
self._distributed_table_creation_lock = threading.Lock()

if not save_context.in_save_context():
    self._maybe_build_distributed_table()
