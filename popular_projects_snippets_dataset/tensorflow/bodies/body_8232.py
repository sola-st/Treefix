# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py
"""Wait for all cluster to exit with a time out."""
waiting_time = 0
exit_process_count = 0
# This addition to mitigate the fact that our step time is too short in test
while exit_process_count != CLUSTER_SIZE and waiting_time < max(
    grace_period + 15, MAX_WAIT_TIME):
    exit_process_count = 0
    for worker_id in range(CLUSTER_SIZE):
        if not mpr.process_exists('worker', worker_id):
            exit_process_count += 1
    waiting_time += 1
    time.sleep(1)

if waiting_time == max(grace_period + 5, 40):
    raise RuntimeError('Waited long but at least one worker still exist. '
                       'Considering size of our model, this should not'
                       ' happen.')
