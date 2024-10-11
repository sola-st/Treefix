# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
expected = "versions { producer: %d min_consumer: %d };\n%s" % (
    producer, min_consumer, expected)
self.assertProtoEquals(expected, actual, msg=msg)
