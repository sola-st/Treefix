# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Call the function if param is callable."""
exit(param() if callable(param) else param)
