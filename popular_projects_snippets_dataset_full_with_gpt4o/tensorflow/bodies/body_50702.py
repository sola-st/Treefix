# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("non_blocking_close")
sw = self._FileWriter(test_dir)
# Sleep 1.2 seconds to make sure event queue is empty.
time.sleep(1.2)
time_before_close = time.time()
sw.close()
self.assertRecent(time_before_close)
