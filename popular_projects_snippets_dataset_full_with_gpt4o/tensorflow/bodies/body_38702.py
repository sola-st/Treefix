# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
n_threads = 4
threads = []
results = []
for _ in range(n_threads):
    session = self.session(graph=ops.Graph(), use_gpu=True)
    results.append(set())
    args = (session, results[-1])
    threads.append(threading.Thread(target=self._run_session, args=args))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

flat_results = set(itertools.chain(*results))
self.assertEqual(1,
                 len(flat_results),
                 'Expected single value, got %r' % flat_results)
