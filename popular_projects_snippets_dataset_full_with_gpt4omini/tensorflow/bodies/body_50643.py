# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
event.wall_time = time.time()
if step is not None:
    event.step = int(step)
self.event_writer.add_event(event)
