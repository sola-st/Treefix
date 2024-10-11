# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
# only switch class if generic(ExcelWriter)
if cls is ExcelWriter:
    if engine is None or (isinstance(engine, str) and engine == "auto"):
        if isinstance(path, str):
            ext = os.path.splitext(path)[-1][1:]
        else:
            ext = "xlsx"

        try:
            engine = config.get_option(f"io.excel.{ext}.writer", silent=True)
            if engine == "auto":
                engine = get_default_engine(ext, mode="writer")
        except KeyError as err:
            raise ValueError(f"No engine for filetype: '{ext}'") from err

            # for mypy
    assert engine is not None
    cls = get_writer(engine)

exit(object.__new__(cls))
