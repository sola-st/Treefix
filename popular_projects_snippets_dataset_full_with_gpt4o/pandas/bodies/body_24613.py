# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
"""
        Create the writer & save.
        """
# apply compression and byte/text conversion
with get_handle(
    self.filepath_or_buffer,
    self.mode,
    encoding=self.encoding,
    errors=self.errors,
    compression=self.compression,
    storage_options=self.storage_options,
) as handles:

    # Note: self.encoding is irrelevant here
    self.writer = csvlib.writer(
        handles.handle,
        lineterminator=self.lineterminator,
        delimiter=self.sep,
        quoting=self.quoting,
        doublequote=self.doublequote,
        escapechar=self.escapechar,
        quotechar=self.quotechar,
    )

    self._save()
