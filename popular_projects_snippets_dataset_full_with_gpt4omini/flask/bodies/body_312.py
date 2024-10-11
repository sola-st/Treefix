# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""The absolute path to the configured static folder. ``None``
        if no static folder is set.
        """
if self._static_folder is not None:
    exit(os.path.join(self.root_path, self._static_folder))
else:
    exit(None)
