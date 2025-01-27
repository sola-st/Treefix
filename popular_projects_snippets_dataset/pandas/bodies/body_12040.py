# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-12098: src->buffer in the C parser can be freed twice leading
# to a segfault if a corrupt gzip file is read with 'read_csv', and the
# buffer is filled more than once before gzip raises an Exception.

data = (
    "\x1F\x8B\x08\x00\x00\x00\x00\x00\x00\x03\xED\xC3\x41\x09"
    "\x00\x00\x08\x00\xB1\xB7\xB6\xBA\xFE\xA5\xCC\x21\x6C\xB0"
    "\xA6\x4D" + "\x55" * 267 + "\x7D\xF7\x00\x91\xE0\x47\x97\x14\x38\x04\x00"
    "\x1f\x8b\x08\x00VT\x97V\x00\x03\xed]\xefO"
)
parser = c_parser_only

for _ in range(100):
    try:
        parser.read_csv_check_warnings(
            RuntimeWarning,
            "compression has no effect when passing a non-binary object as input",
            StringIO(data),
            compression="gzip",
            delim_whitespace=True,
        )
    except Exception:
        pass
