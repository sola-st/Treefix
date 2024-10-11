# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# gh-16530: the file-like need not have a "next" or "__next__"
# attribute despite having an "__iter__" attribute.
#
# NOTE: This is only true for the C engine, not Python engine.
class NoNextBuffer(StringIO):
    def __next__(self):
        raise AttributeError("No next method")

    next = __next__

parser = c_parser_only
data = "a\n1"

expected = DataFrame({"a": [1]})
result = parser.read_csv(NoNextBuffer(data))

tm.assert_frame_equal(result, expected)
