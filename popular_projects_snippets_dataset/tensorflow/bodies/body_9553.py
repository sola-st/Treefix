# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline_test.py
# Check that the supplied string is valid JSON.
trace = json.loads(chrome_trace_format)
# It should have a top-level key containing events.
self.assertTrue('traceEvents' in trace)
# Every event in the list should have a 'ph' field.
for event in trace['traceEvents']:
    self.assertTrue('ph' in event)
