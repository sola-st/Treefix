# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
# If a subclass overrides setUp and doesn't call the parent class's setUp,
# then we may not have set the start time.
if self._test_start_time is not None:
    logging.info("time(%s): %ss", self.id(),
                 round(time.time() - self._test_start_time, 2))

for thread in self._threads:
    thread.check_termination()

self._ClearCachedSession()
super().tearDown()
