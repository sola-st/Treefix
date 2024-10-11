# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
self.fmt = formatter

self.obj = self.fmt.frame

self.filepath_or_buffer = path_or_buf
self.encoding = encoding
self.compression: CompressionOptions = compression
self.mode = mode
self.storage_options = storage_options

self.sep = sep
self.index_label = self._initialize_index_label(index_label)
self.errors = errors
self.quoting = quoting or csvlib.QUOTE_MINIMAL
self.quotechar = self._initialize_quotechar(quotechar)
self.doublequote = doublequote
self.escapechar = escapechar
self.lineterminator = lineterminator or os.linesep
self.date_format = date_format
self.cols = self._initialize_columns(cols)
self.chunksize = self._initialize_chunksize(chunksize)
