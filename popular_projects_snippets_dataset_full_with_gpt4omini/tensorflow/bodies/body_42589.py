# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
counter1 = monitoring.Counter('test/same_counter', 'test counter')  # pylint: disable=unused-variable
with self.assertRaises(errors.AlreadyExistsError):
    counter2 = monitoring.Counter('test/same_counter', 'test counter')  # pylint: disable=unused-variable
