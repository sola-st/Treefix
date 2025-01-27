# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# see gh-6607
data = "a b c\n1 2 3"
msg = "does not support"

# specify C engine with unsupported options (raise)
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), engine="c", sep=None, delim_whitespace=False)
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), engine="c", sep=r"\s")
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), engine="c", sep="\t", quotechar=chr(128))
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), engine="c", skipfooter=1)

# specify C-unsupported options without python-unsupported options
with tm.assert_produces_warning(parsers.ParserWarning):
    read_csv(StringIO(data), sep=None, delim_whitespace=False)
with tm.assert_produces_warning(parsers.ParserWarning):
    read_csv(StringIO(data), sep=r"\s")
with tm.assert_produces_warning(parsers.ParserWarning):
    read_csv(StringIO(data), sep="\t", quotechar=chr(128))
with tm.assert_produces_warning(parsers.ParserWarning):
    read_csv(StringIO(data), skipfooter=1)

text = """                      A       B       C       D        E
one two three   four
a   b   10.0032 5    -0.5109 -2.3358 -0.4645  0.05076  0.3640
a   q   20      4     0.4473  1.4152  0.2834  1.00661  0.1744
x   q   30      3    -0.6662 -0.5243 -0.3580  0.89145  2.5838"""
msg = "Error tokenizing data"

with pytest.raises(ParserError, match=msg):
    read_csv(StringIO(text), sep="\\s+")
with pytest.raises(ParserError, match=msg):
    read_csv(StringIO(text), engine="c", sep="\\s+")

msg = "Only length-1 thousands markers supported"
data = """A|B|C
1|2,334|5
10|13|10.
"""
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), thousands=",,")
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), thousands="")

msg = "Only length-1 line terminators supported"
data = "a,b,c~~1,2,3~~4,5,6"
with pytest.raises(ValueError, match=msg):
    read_csv(StringIO(data), lineterminator="~~")
