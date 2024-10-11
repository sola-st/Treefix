# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# Fork ten threads that use their thread-local default graph.
threads = []
constructed_events = [threading.Event() for _ in range(10)]
continue_event = threading.Event()
for i, constructed_event in enumerate(constructed_events):
    t = self.checkedThread(
        target=self._testDefaultGraphInThread,
        args=(constructed_event, continue_event, i))
    threads.append(t)
for t in threads:
    t.start()
for constructed_event in constructed_events:
    constructed_event.wait()
continue_event.set()
for t in threads:
    t.join()
