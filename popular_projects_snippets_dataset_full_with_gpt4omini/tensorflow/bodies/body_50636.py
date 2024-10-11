# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds a `Summary` protocol buffer to the event file.

    This method wraps the provided summary in an `Event` protocol buffer
    and adds it to the event file.

    You can pass the result of evaluating any summary op, using
    `tf.Session.run` or
    `tf.Tensor.eval`, to this
    function. Alternatively, you can pass a `tf.compat.v1.Summary` protocol
    buffer that you populate with your own data. The latter is
    commonly done to report evaluation results in event files.

    Args:
      summary: A `Summary` protocol buffer, optionally serialized as a string.
      global_step: Number. Optional global step value to record with the
        summary.
    """
if isinstance(summary, bytes):
    summ = summary_pb2.Summary()
    summ.ParseFromString(summary)
    summary = summ

# We strip metadata from values with tags that we have seen before in order
# to save space - we just store the metadata on the first value with a
# specific tag.
for value in summary.value:
    if not value.metadata:
        continue

    if value.tag in self._seen_summary_tags:
        # This tag has been encountered before. Strip the metadata.
        value.ClearField("metadata")
        continue

    # We encounter a value with a tag we have not encountered previously. And
    # it has metadata. Remember to strip metadata from future values with this
    # tag string.
    self._seen_summary_tags.add(value.tag)

event = event_pb2.Event(summary=summary)
self._add_event(event, global_step)
