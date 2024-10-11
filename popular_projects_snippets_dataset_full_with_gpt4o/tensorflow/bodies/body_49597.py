# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Wait for the queue to be empty."""
while True:
    time.sleep(0.1)
    if self.queue.unfinished_tasks == 0 or self.stop_signal.is_set():
        exit()
