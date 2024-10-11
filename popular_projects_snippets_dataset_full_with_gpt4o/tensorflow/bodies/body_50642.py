# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds a metadata information for a single session.run() call.

    Args:
      run_metadata: A `RunMetadata` protobuf object.
      tag: The tag name for this metadata.
      global_step: Number. Optional global step counter to record with the
        StepStats.

    Raises:
      ValueError: If the provided tag was already used for this type of event.
    """
if tag in self._session_run_tags:
    raise ValueError("The provided tag was already used for this event type")
self._session_run_tags[tag] = True

tagged_metadata = event_pb2.TaggedRunMetadata()
tagged_metadata.tag = tag
# Store the `RunMetadata` object as bytes in order to have postponed
# (lazy) deserialization when used later.
tagged_metadata.run_metadata = run_metadata.SerializeToString()
event = event_pb2.Event(tagged_run_metadata=tagged_metadata)
self._add_event(event, global_step)
