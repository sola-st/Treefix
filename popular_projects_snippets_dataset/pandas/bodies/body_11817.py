# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_verbose.py
parser = all_parsers
data = """a,b,c,d
one,1,2,3
one,1,2,3
,1,2,3
one,1,2,3
,1,2,3
,1,2,3
one,1,2,3
two,1,2,3"""

# Engines are verbose in different ways.
parser.read_csv(StringIO(data), verbose=True)
captured = capsys.readouterr()

if parser.engine == "c":
    assert "Tokenization took:" in captured.out
    assert "Parser memory cleanup took:" in captured.out
else:  # Python engine
    assert captured.out == "Filled 3 NA values in column a\n"
