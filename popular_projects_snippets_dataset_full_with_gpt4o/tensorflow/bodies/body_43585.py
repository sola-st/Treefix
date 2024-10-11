# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util_test.py
time.sleep(random.random() * 0.1)
group_id = thread_id % num_groups
with lock.group(group_id):
    time.sleep(random.random() * 0.1)
    self.assertGreater(lock._group_member_counts[group_id], 0)
    for g, c in enumerate(lock._group_member_counts):
        if g != group_id:
            self.assertEqual(0, c)
    finished.add(thread_id)
