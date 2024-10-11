# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/heartbeat.py
logging.info('Stopping the heartbeat thread')
_heartbeat_timer.set()
# Give the threads some time to clean up.
time.sleep(max(period // 10, 2))
