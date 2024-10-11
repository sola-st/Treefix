# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Creates a `CsvDataset` by reading and decoding CSV files.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      record_defaults: A list of default values for the CSV fields. Each item in
        the list is either a valid CSV `DType` (float32, float64, int32, int64,
        string), or a `Tensor` object with one of the above types. One per
        column of CSV data, with either a scalar `Tensor` default value for the
        column if it is optional, or `DType` or empty `Tensor` if required. If
        both this and `select_columns` are specified, these must have the same
        lengths, and `column_defaults` is assumed to be sorted in order of
        increasing column index. If both this and 'exclude_cols' are specified,
        the sum of lengths of record_defaults and exclude_cols should equal
        the total number of columns in the CSV file.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no
        compression.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer while reading files. Defaults to 4MB.
      header: (Optional.) A `tf.bool` scalar indicating whether the CSV file(s)
        have header line(s) that should be skipped when parsing. Defaults to
        `False`.
      field_delim: (Optional.) A `tf.string` scalar containing the delimiter
        character that separates fields in a record. Defaults to `","`.
      use_quote_delim: (Optional.) A `tf.bool` scalar. If `False`, treats
        double quotation marks as regular characters inside of string fields
        (ignoring RFC 4180, Section 2, Bullet 5). Defaults to `True`.
      na_value: (Optional.) A `tf.string` scalar indicating a value that will
        be treated as NA/NaN.
      select_cols: (Optional.) A sorted list of column indices to select from
        the input data. If specified, only this subset of columns will be
        parsed. Defaults to parsing all columns. At most one of `select_cols`
        and `exclude_cols` can be specified.
      exclude_cols: (Optional.) A sorted list of column indices to exclude from
        the input data. If specified, only the complement of this set of column
        will be parsed. Defaults to parsing all columns. At most one of
        `select_cols` and `exclude_cols` can be specified.

    Raises:
       InvalidArgumentError: If exclude_cols is not None and
           len(exclude_cols) + len(record_defaults) does not match the total
           number of columns in the file(s)


    """
self._filenames = ops.convert_to_tensor(
    filenames, dtype=dtypes.string, name="filenames")
self._compression_type = convert.optional_param_to_tensor(
    "compression_type",
    compression_type,
    argument_default="",
    argument_dtype=dtypes.string)
record_defaults = [
    constant_op.constant([], dtype=x)
    if not tensor_util.is_tf_type(x) and x in _ACCEPTABLE_CSV_TYPES else x
    for x in record_defaults
]
self._record_defaults = ops.convert_n_to_tensor(
    record_defaults, name="record_defaults")
self._buffer_size = convert.optional_param_to_tensor(
    "buffer_size", buffer_size, _DEFAULT_READER_BUFFER_SIZE_BYTES)
self._header = ops.convert_to_tensor(
    header, dtype=dtypes.bool, name="header")
self._field_delim = ops.convert_to_tensor(
    field_delim, dtype=dtypes.string, name="field_delim")
self._use_quote_delim = ops.convert_to_tensor(
    use_quote_delim, dtype=dtypes.bool, name="use_quote_delim")
self._na_value = ops.convert_to_tensor(
    na_value, dtype=dtypes.string, name="na_value")
self._select_cols = convert.optional_param_to_tensor(
    "select_cols",
    select_cols,
    argument_default=[],
    argument_dtype=dtypes.int64,
)
self._exclude_cols = convert.optional_param_to_tensor(
    "exclude_cols",
    exclude_cols,
    argument_default=[],
    argument_dtype=dtypes.int64,
)
self._element_spec = tuple(
    tensor_spec.TensorSpec([], d.dtype) for d in self._record_defaults)
variant_tensor = gen_experimental_dataset_ops.csv_dataset_v2(
    filenames=self._filenames,
    record_defaults=self._record_defaults,
    buffer_size=self._buffer_size,
    header=self._header,
    output_shapes=self._flat_shapes,
    field_delim=self._field_delim,
    use_quote_delim=self._use_quote_delim,
    na_value=self._na_value,
    select_cols=self._select_cols,
    exclude_cols=self._exclude_cols,
    compression_type=self._compression_type)
super(CsvDatasetV2, self).__init__(variant_tensor)
