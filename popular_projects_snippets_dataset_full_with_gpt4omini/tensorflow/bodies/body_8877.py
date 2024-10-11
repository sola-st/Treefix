# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
closure_queue = coordinator_lib._CoordinatedClosureQueue()

def func():
    logging.info('func running')

coord = coordinator.Coordinator(clean_stop_exception_types=[])

def process_queue():
    with coord.stop_on_exception():
        closure_queue.get()
        closure_queue.mark_finished()

closure_queue.put(ClosureWithOutput(func, closure_queue._cancellation_mgr))
t = threading.Thread(target=process_queue)
t.start()
coord.join([t])

# This test asserts that waiting at the time the function has been processed
# doesn't time out.
closure_queue.wait()
