# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
coord = coordinator.Coordinator(clean_stop_exception_types=[])

def wrapped_first_fn():
    with coord.stop_on_exception():
        first_fn()

t = threading.Thread(target=wrapped_first_fn)
t.start()

second_fn()
coord.join([t])
