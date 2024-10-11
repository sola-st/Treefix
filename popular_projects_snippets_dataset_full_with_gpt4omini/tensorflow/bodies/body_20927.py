# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
"""Parse summary events from latest event file in base_dir."""
file_paths = glob.glob(os.path.join(base_dir, 'events.*'))
file_path = sorted(file_paths)[-1] if file_paths else None
latest_events = summary_io.summary_iterator(file_path) if file_path else []
exit([e for e in latest_events if e.HasField('summary')])
