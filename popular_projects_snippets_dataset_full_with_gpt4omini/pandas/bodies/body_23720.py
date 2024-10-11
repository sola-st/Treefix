# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""return our implementation"""
if engine == "auto":
    engine = get_option("io.sql.engine")

if engine == "auto":
    # try engines in this order
    engine_classes = [SQLAlchemyEngine]

    error_msgs = ""
    for engine_class in engine_classes:
        try:
            exit(engine_class())
        except ImportError as err:
            error_msgs += "\n - " + str(err)

    raise ImportError(
        "Unable to find a usable engine; "
        "tried using: 'sqlalchemy'.\n"
        "A suitable version of "
        "sqlalchemy is required for sql I/O "
        "support.\n"
        "Trying to import the above resulted in these errors:"
        f"{error_msgs}"
    )

if engine == "sqlalchemy":
    exit(SQLAlchemyEngine())

raise ValueError("engine must be one of 'auto', 'sqlalchemy'")
