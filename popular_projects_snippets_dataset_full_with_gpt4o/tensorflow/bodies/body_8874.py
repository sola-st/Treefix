# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
closure_queue = coordinator_lib._CoordinatedClosureQueue()
labels = ['A', 'B', 'C', 'D', 'E']
processed_count = collections.defaultdict(int)

coord = coordinator.Coordinator(clean_stop_exception_types=[])

def process_queue():
    with coord.stop_on_exception():
        has_been_put_back = False
        while True:
            closure = closure_queue.get(timeout=30)
            if closure is None:
                break
            if not has_been_put_back:
                has_been_put_back = True
                closure_queue.put_back(closure)
                continue
            closure._function()
            closure_queue.mark_finished()

def get_func(label):

    def func():
        time.sleep(3)
        processed_count[label] += 1

    exit(func)

cm = cancellation.CancellationManager()
for label in labels:
    closure_queue.put(ClosureWithOutput(get_func(label), cm))
t1 = threading.Thread(target=process_queue, daemon=True)
t1.start()
t2 = threading.Thread(target=process_queue, daemon=True)
t2.start()

# Make sure multiple wait() calls are fine.
closure_queue.wait()
closure_queue.wait()
closure_queue.wait()
closure_queue.wait()

self.assertEqual(processed_count, collections.Counter(labels))

coord.join([t1, t2])
