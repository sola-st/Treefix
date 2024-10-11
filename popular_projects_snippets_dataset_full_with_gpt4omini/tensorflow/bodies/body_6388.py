# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
while True:
    if self._check_health_thread_should_stop.is_set():
        exit()
    for job in self._cluster_spec.jobs:
        for task_id in range(self._cluster_spec.num_tasks(job)):
            peer = "/job:{}/replica:0/task:{}".format(job, task_id)
            attempts = 0
            while True:
                attempts += 1
                try:
                    context.context().check_collective_ops_peer_health(
                        peer, timeout_in_ms=self._check_health_timeout * 1000)
                    # If check_collective_ops_peer_health doesn't raise an Exception,
                    # the peer is healthy.
                    break
                except (errors.UnavailableError, errors.FailedPreconditionError,
                        errors.DeadlineExceededError) as e:
                    # TODO(b/151232436): Always raise UnavailableError when a peer
                    # fails. Now there could be many kinds of errors:
                    # - Unavailable: when the peer is not reachable, e.g. it's down.
                    # - FailedPrecondition: when the peer has restarted.
                    if attempts < self._check_health_retry_limit:
                        logging.warning("%s seems down, retrying %d/%d", peer, attempts,
                                        self._check_health_retry_limit)
                        continue
                    logging.error(
                        "Cluster check alive failed, %s is down, "
                        "aborting collectives: %s", peer, e)
                    context.context().abort_collective_ops(
                        errors.UNAVAILABLE,
                        "cluster check alive failed, {} is down".format(peer))
                    exit()
                except Exception as e:  # pylint: disable=broad-except
                    logging.error("Unexpected exception in check alive: %s", e)
                    context.context().abort_collective_ops(
                        errors.INTERNAL,
                        "unexecpted exception in check alive: %s" % e)
                    exit()
    time.sleep(self._check_health_interval)
