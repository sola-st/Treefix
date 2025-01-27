# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Read a tflite model assuming the given flatbuffer schema.

    If `input_file` is in bin, then we must use flatc to convert the schema
    from binary to json.

    Args:
      input_file: a binary (flatbuffer) or json file to read from. Extension
        must  be `.tflite`, `.bin`, or `.json` for FlatBuffer Binary or
        FlatBuffer JSON.
      schema: which schema to use for reading
      raw_binary: whether to assume raw_binary (versions previous to v3)
        that lacked file_identifier require this.

    Raises:
      RuntimeError: 1. When flatc cannot be invoked.
                    2. When json file does not exists.
      ValueError: When the extension is not json or bin.

    Returns:
      A dictionary representing the read tflite model.
    """
raw_binary = ["--raw-binary"] if raw_binary else []
with TemporaryDirectoryResource() as tempdir:
    basename = os.path.basename(input_file)
    basename_no_extension, extension = os.path.splitext(basename)
    if extension in [".bin", ".tflite"]:
        # Convert to json using flatc
        returncode = subprocess.call([
            self._flatc_path,
            "-t",
            "--strict-json",
            "--defaults-json",
        ] + raw_binary + ["-o", tempdir, schema, "--", input_file])
        if returncode != 0:
            raise RuntimeError("flatc failed to convert from binary to json.")
        json_file = os.path.join(tempdir, basename_no_extension + ".json")
        if not os.path.exists(json_file):
            raise RuntimeError("Could not find %r" % json_file)
    elif extension == ".json":
        json_file = input_file
    else:
        raise ValueError("Invalid extension on input file %r" % input_file)
    exit(json.load(open(json_file)))
