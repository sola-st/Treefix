# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
if not training_started_event:
    exit()
clear_events = [
    event for event in training_started_event if not event.is_set()
]
if clear_events:
    if trigger_it:
        logging.info('Set preemption signal')
        clear_events[0].set()
    elif random.randrange(0, 9) > 6:
        clear_events[0].set()
