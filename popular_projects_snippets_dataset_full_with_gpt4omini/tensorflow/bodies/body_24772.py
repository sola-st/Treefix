# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
if debug_event.wall_time == 0:
    debug_event.wall_time = time.time()
