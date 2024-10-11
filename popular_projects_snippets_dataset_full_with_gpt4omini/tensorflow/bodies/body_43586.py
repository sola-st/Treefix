# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util_test.py
lock = lock_util.GroupLock(num_groups)
num_threads = 10
finished = set()

def thread_fn(thread_id):
    time.sleep(random.random() * 0.1)
    group_id = thread_id % num_groups
    with lock.group(group_id):
        time.sleep(random.random() * 0.1)
        self.assertGreater(lock._group_member_counts[group_id], 0)
        for g, c in enumerate(lock._group_member_counts):
            if g != group_id:
                self.assertEqual(0, c)
        finished.add(thread_id)

threads = [
    self.checkedThread(target=thread_fn, args=(i,))
    for i in range(num_threads)
]

for i in range(num_threads):
    threads[i].start()
for i in range(num_threads):
    threads[i].join()

self.assertEqual(set(range(num_threads)), finished)
