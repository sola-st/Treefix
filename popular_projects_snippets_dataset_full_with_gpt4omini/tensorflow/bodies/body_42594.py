# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
counter = monitoring.Counter('test/ctxmgr', 'test context manager', 'slot')
with monitoring.MonitoredTimer(counter.get_cell('long')):
    time.sleep(0.01)
    with monitoring.MonitoredTimer(counter.get_cell('short')):
        time.sleep(0.01)
self.assertGreater(
    counter.get_cell('long').value(),
    counter.get_cell('short').value())
