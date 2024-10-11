# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
thread_count = 10
queue = coordinator_lib._CoordinatedClosureQueue()

# Each thread performs 20 queue actions: 10 are `put_back` and 10 are
# `mark_finished`.
action_count = 20

def func():
    for i in range(action_count):
        closure = queue.get()
        if i % 2 == 0:
            queue.put_back(closure)
        else:
            queue.mark_finished()

threads = [threading.Thread(target=func) for i in range(thread_count)]
for t in threads:
    t.start()

for _ in range(thread_count * action_count // 2):
    queue.put(self._create_closure(queue._cancellation_mgr))
queue.wait()
self.assertTrue(queue.done())
