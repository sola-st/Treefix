# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
counter = monitoring.Counter('test/funcdecorator', 'test func decorator')

@monitoring.monitored_timer(counter.get_cell())
def timed_function(seconds):
    time.sleep(seconds)

timed_function(0.001)
self.assertGreater(counter.get_cell().value(), 1000)
