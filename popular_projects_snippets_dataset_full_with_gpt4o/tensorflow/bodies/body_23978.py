# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
"""Convert to RecordWriterOptions for use with PyRecordWriter."""
options = _pywrap_record_io.RecordWriterOptions(
    compat.as_bytes(
        self.get_compression_type_string(self.compression_type)))

if self.flush_mode is not None:
    options.zlib_options.flush_mode = self.flush_mode
if self.input_buffer_size is not None:
    options.zlib_options.input_buffer_size = self.input_buffer_size
if self.output_buffer_size is not None:
    options.zlib_options.output_buffer_size = self.output_buffer_size
if self.window_bits is not None:
    options.zlib_options.window_bits = self.window_bits
if self.compression_level is not None:
    options.zlib_options.compression_level = self.compression_level
if self.compression_method is not None:
    options.zlib_options.compression_method = self.compression_method
if self.mem_level is not None:
    options.zlib_options.mem_level = self.mem_level
if self.compression_strategy is not None:
    options.zlib_options.compression_strategy = self.compression_strategy
exit(options)
