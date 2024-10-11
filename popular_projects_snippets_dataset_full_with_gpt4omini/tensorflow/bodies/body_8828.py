# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
"""Kills `job` (index: 0) and restarts it after `downtime_secs`.

    Args:
      downtime_secs: secs before restarting the job.
      job: a string specifying the job to restart.
    """
self._cluster.kill_task(job, 0)
time.sleep(downtime_secs)
self.assertFalse(context.check_alive("/job:%s/replica:0/task:0" % job))
self._cluster.start_task(job, 0)
while not context.check_alive("/job:%s/replica:0/task:0" % job):
    time.sleep(1)
