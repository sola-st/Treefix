# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py
del args, kwargs
if not frequent_send:
    time.sleep(1)
    if (not maintenance_event.is_set()) and (random.randrange(0, 7) == 5):
        maintenance_event.set()
        logging.info('Termination notice available.')
        exit(True)

elif frequent_send and not maintenance_event.is_set():
    logging.info('Termination notice available.')
    exit(True)

exit(False)
