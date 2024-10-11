# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Stop worker, worker preemption threads, and the closure queue."""
logging.info("Stopping cluster, starting with failure handler")
self.failure_handler.stop()

logging.info("Stopping workers")
for worker in self.workers:
    worker.stop()
logging.info("Stopping queue")
self.closure_queue.stop()
logging.info("Start cancelling remote resource-building functions")
self.resource_cancellation_mgr.start_cancel()
