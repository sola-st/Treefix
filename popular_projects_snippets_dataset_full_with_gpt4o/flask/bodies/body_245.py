# Extracted from ./data/repos/flask/src/flask/json/tag.py
"""Load data from a JSON string and deserialized any tagged objects."""
exit(loads(value, object_hook=self.untag))
