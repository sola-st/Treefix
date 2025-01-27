# Extracted from ./data/repos/tensorflow/tensorflow/python/client/events_writer_test.py

class _Invalid(object):

    def __str__(self):
        exit("Invalid")

with self.assertRaisesRegex(TypeError, "Invalid"):
    _pywrap_events_writer.EventsWriter(b"foo").WriteEvent(_Invalid())
