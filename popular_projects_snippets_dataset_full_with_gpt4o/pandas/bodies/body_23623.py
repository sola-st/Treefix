# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Export DataFrame object to Stata dta format.
        """
with get_handle(
    self._fname,
    "wb",
    compression=self._compression,
    is_text=False,
    storage_options=self.storage_options,
) as self.handles:

    if self.handles.compression["method"] is not None:
        # ZipFile creates a file (with the same name) for each write call.
        # Write it first into a buffer and then write the buffer to the ZipFile.
        self._output_file, self.handles.handle = self.handles.handle, BytesIO()
        self.handles.created_handles.append(self.handles.handle)

    try:
        self._write_header(
            data_label=self._data_label, time_stamp=self._time_stamp
        )
        self._write_map()
        self._write_variable_types()
        self._write_varnames()
        self._write_sortlist()
        self._write_formats()
        self._write_value_label_names()
        self._write_variable_labels()
        self._write_expansion_fields()
        self._write_characteristics()
        records = self._prepare_data()
        self._write_data(records)
        self._write_strls()
        self._write_value_labels()
        self._write_file_close_tag()
        self._write_map()
        self._close()
    except Exception as exc:
        self.handles.close()
        if isinstance(self._fname, (str, os.PathLike)) and os.path.isfile(
            self._fname
        ):
            try:
                os.unlink(self._fname)
            except OSError:
                warnings.warn(
                    f"This save was not successful but {self._fname} could not "
                    "be deleted. This file is not valid.",
                    ResourceWarning,
                    stacklevel=find_stack_level(),
                )
        raise exc
