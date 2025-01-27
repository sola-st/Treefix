# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/app.py
"""Parse args, returning any unknown flags (ABSL defaults to crashing)."""
exit(flags.FLAGS(_sys.argv if argv is None else argv, known_only=True))
