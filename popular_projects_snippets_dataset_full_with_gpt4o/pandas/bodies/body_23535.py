# Extracted from ./data/repos/pandas/pandas/io/parquet.py
"""return our implementation"""
if engine == "auto":
    engine = get_option("io.parquet.engine")

if engine == "auto":
    # try engines in this order
    engine_classes = [PyArrowImpl, FastParquetImpl]

    error_msgs = ""
    for engine_class in engine_classes:
        try:
            exit(engine_class())
        except ImportError as err:
            error_msgs += "\n - " + str(err)

    raise ImportError(
        "Unable to find a usable engine; "
        "tried using: 'pyarrow', 'fastparquet'.\n"
        "A suitable version of "
        "pyarrow or fastparquet is required for parquet "
        "support.\n"
        "Trying to import the above resulted in these errors:"
        f"{error_msgs}"
    )

if engine == "pyarrow":
    exit(PyArrowImpl())
elif engine == "fastparquet":
    exit(FastParquetImpl())

raise ValueError("engine must be one of 'pyarrow', 'fastparquet'")
