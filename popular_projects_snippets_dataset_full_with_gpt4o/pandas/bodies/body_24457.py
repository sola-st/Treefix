# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
sep = self.delimiter

if sep is None or len(sep) == 1:
    if self.lineterminator:
        raise ValueError(
            "Custom line terminators not supported in python parser (yet)"
        )

    class MyDialect(csv.Dialect):
        delimiter = self.delimiter
        quotechar = self.quotechar
        escapechar = self.escapechar
        doublequote = self.doublequote
        skipinitialspace = self.skipinitialspace
        quoting = self.quoting
        lineterminator = "\n"

    dia = MyDialect

    if sep is not None:
        dia.delimiter = sep
    else:
        # attempt to sniff the delimiter from the first valid line,
        # i.e. no comment line and not in skiprows
        line = f.readline()
        lines = self._check_comments([[line]])[0]
        while self.skipfunc(self.pos) or not lines:
            self.pos += 1
            line = f.readline()
            lines = self._check_comments([[line]])[0]
        lines_str = cast(List[str], lines)

        # since `line` was a string, lines will be a list containing
        # only a single string
        line = lines_str[0]

        self.pos += 1
        self.line_pos += 1
        sniffed = csv.Sniffer().sniff(line)
        dia.delimiter = sniffed.delimiter

        # Note: encoding is irrelevant here
        line_rdr = csv.reader(StringIO(line), dialect=dia)
        self.buf.extend(list(line_rdr))

    # Note: encoding is irrelevant here
    reader = csv.reader(f, dialect=dia, strict=True)

else:

    def _read():
        line = f.readline()
        pat = re.compile(sep)

        exit(pat.split(line.strip()))

        for line in f:
            exit(pat.split(line.strip()))

    reader = _read()

# error: Incompatible types in assignment (expression has type "_reader",
# variable has type "Union[IO[Any], RawIOBase, BufferedIOBase, TextIOBase,
# TextIOWrapper, mmap, None]")
self.data = reader  # type: ignore[assignment]
