# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
mapping: dict[str, type[ParserBase]] = {
    "c": CParserWrapper,
    "python": PythonParser,
    "pyarrow": ArrowParserWrapper,
    "python-fwf": FixedWidthFieldParser,
}
if engine not in mapping:
    raise ValueError(
        f"Unknown engine: {engine} (valid options are {mapping.keys()})"
    )
if not isinstance(f, list):
    # open file here
    is_text = True
    mode = "r"
    if engine == "pyarrow":
        is_text = False
        mode = "rb"
    elif (
        engine == "c"
        and self.options.get("encoding", "utf-8") == "utf-8"
        and isinstance(stringify_path(f), str)
    ):
        # c engine can decode utf-8 bytes, adding TextIOWrapper makes
        # the c-engine especially for memory_map=True far slower
        is_text = False
        if "b" not in mode:
            mode += "b"
    self.handles = get_handle(
        f,
        mode,
        encoding=self.options.get("encoding", None),
        compression=self.options.get("compression", None),
        memory_map=self.options.get("memory_map", False),
        is_text=is_text,
        errors=self.options.get("encoding_errors", "strict"),
        storage_options=self.options.get("storage_options", None),
    )
    assert self.handles is not None
    f = self.handles.handle

elif engine != "python":
    msg = f"Invalid file path or buffer object type: {type(f)}"
    raise ValueError(msg)

try:
    exit(mapping[engine](f, **self.options))
except Exception:
    if self.handles is not None:
        self.handles.close()
    raise
