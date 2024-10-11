# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Constructs a table initializer object to populate from a text file.

    It generates one key-value pair per line. The type of table key and
    value are specified by `key_dtype` and `value_dtype`, respectively.
    Similarly the content of the key and value are specified by the key_index
    and value_index.

    - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
      expects data type int64.
    - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
      type string or int64.
    - A value >=0 means use the index (starting at zero) of the split line based
      on `delimiter`.

    Args:
      filename: The filename of the text file to be used for initialization. The
        path must be accessible from wherever the graph is initialized (eg.
        trainer or eval workers). The filename may be a scalar `Tensor`.
      key_dtype: The `key` data type.
      key_index: the index that represents information of a line to get the
        table 'key' values from.
      value_dtype: The `value` data type.
      value_index: the index that represents information of a line to get the
        table 'value' values from.'
      vocab_size: The number of elements in the file, if known.
      delimiter: The delimiter to separate fields in a line.
      name: A name for the operation (optional).
      value_index_offset: A number to add to all indices extracted from the file
        This is useful for cases where a user would like to reserve one or more
        low index values for control characters. For instance, if you would
        like to ensure that no vocabulary item is mapped to index 0 (so you can
        reserve 0 for a masking value), you can set value_index_offset to 1;
        this will mean that the first vocabulary element is mapped to 1
        instead of 0.

    Raises:
      ValueError: when the filename is empty, or when the table key and value
      data types do not match the expected data types.
    """
if not isinstance(filename, ops.Tensor) and not filename:
    raise ValueError("`filename` argument required for tf.lookup.TextFileInitializer")

self._filename_arg = filename
key_dtype = dtypes.as_dtype(key_dtype)
value_dtype = dtypes.as_dtype(value_dtype)

if key_index < -2:
    raise ValueError(f"`key_index` should be >= -2, received: {key_index}.")

if key_index == TextFileIndex.LINE_NUMBER and key_dtype != dtypes.int64:
    raise ValueError("`key_dtype` must be int64 if `key_index` is "
                     f"{TextFileIndex.LINE_NUMBER}, received: {key_dtype}")
if ((key_index == TextFileIndex.WHOLE_LINE) and
    (not key_dtype.is_integer) and (key_dtype != dtypes.string)):
    raise ValueError(
        "`key_dtype` should be either integer or string for `key_index` "
        f"{TextFileIndex.WHOLE_LINE}, received: {key_dtype}")
if value_index < -2:
    raise ValueError("`value_index` should be >= -2, received: "
                     f"{value_index}")

if value_index == TextFileIndex.LINE_NUMBER and value_dtype != dtypes.int64:
    raise ValueError("`value_dtype` must be int64 for `value_index` "
                     f"{TextFileIndex.LINE_NUMBER}, received: {value_dtype}")
if ((value_index == TextFileIndex.WHOLE_LINE) and
    (not value_dtype.is_integer) and (value_dtype != dtypes.string)):
    raise ValueError(
        "`value_dtype` should be either integer or string for `value_index` "
        f"{TextFileIndex.WHOLE_LINE}, received: {value_dtype}")

if (vocab_size is not None) and (vocab_size <= 0):
    raise ValueError(f"`vocab_size` should be > 0, received: {vocab_size}")

self._key_index = key_index
self._value_index = value_index
self._vocab_size = vocab_size
self._delimiter = delimiter
self._name = name
self._filename = self._track_trackable(
    asset.Asset(filename), "_filename")
self._offset = value_index_offset

super(TextFileInitializer, self).__init__(key_dtype, value_dtype)
