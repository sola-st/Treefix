# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
"""Add summary."""
if isinstance(summ, bytes):
    summary_proto = summary_pb2.Summary()
    summary_proto.ParseFromString(summ)
    summ = summary_proto
if current_global_step in self._summaries:
    step_summaries = self._summaries[current_global_step]
else:
    step_summaries = []
    self._summaries[current_global_step] = step_summaries
step_summaries.append(summ)
