# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
while not training_started_event.is_set():
    time.sleep(1)
logging.info('sending sigterm')
training_started_event.set()
os.kill(os.getpid(), signal.SIGTERM)
