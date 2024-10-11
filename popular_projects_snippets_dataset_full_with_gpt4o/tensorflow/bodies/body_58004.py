# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
super(ConverterError, self).__init__(message)
self.errors = []
self._parse_error_message(message)
