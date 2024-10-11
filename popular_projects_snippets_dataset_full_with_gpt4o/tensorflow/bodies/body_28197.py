# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Test multi-threaded access to the same iterator.
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))
get_next = self.getNext(
    self._map_dataset_factory(components, apply_map, count=18))
results = []
with self.cached_session() as sess:
    def iterator_thread():
        while True:
            try:
                results.append(sess.run(get_next()))
            except errors.OutOfRangeError:
                exit()
    threads = [self.checkedThread(target=iterator_thread) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # `results` will contain the same elements components**2
    # repeated 18 times, but in a non-deterministic order. Sort the
    # results, and assert that each element of components**2 is
    # produced 18 times.
    results.sort(key=lambda x: x[0])
    for i in range(7):
        for j in range(18):
            for component, result_component in zip(components,
                                                   results[i * 18 + j]):
                self.assertAllEqual(component[i]**2, result_component)
