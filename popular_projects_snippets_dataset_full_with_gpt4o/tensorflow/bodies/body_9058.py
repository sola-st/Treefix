# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Delay if corresponding env vars are set."""
# If the following two env vars variables are set. Scheduling for workers
# will start in a staggered manner. Worker i will wait for
# `TF_COORDINATOR_SCHEDULE_START_DELAY` * i seconds, not exceeding
# `TF_COORDINATOR_SCHEDULE_START_DELAY_MAX`.
delay_secs = int(os.environ.get("TF_COORDINATOR_SCHEDULE_START_DELAY", "0"))
delay_secs *= self.worker_index
delay_cap = int(
    os.environ.get("TF_COORDINATOR_SCHEDULE_START_DELAY_MAX", "0"))
if delay_cap:
    delay_secs = min(delay_secs, delay_cap)
if delay_secs > 0:
    logging.info(" Worker %d sleeping for %d seconds before running function",
                 self.worker_index, delay_secs)
time.sleep(delay_secs)
