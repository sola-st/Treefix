# Extracted from ./data/repos/flask/src/flask/scaffold.py
if value is not None:
    value = os.fspath(value).rstrip(r"\/")

self._static_folder = value
