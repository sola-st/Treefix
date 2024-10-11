# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
parser = all_parsers
data = """\
label1,label2,label3
index1,"a,c,e
index2,b,d,f
"""

dia = csv.excel()
dia.quoting = csv.QUOTE_NONE
df = parser.read_csv(StringIO(data), dialect=dia)

data = """\
label1,label2,label3
index1,a,c,e
index2,b,d,f
"""
exp = parser.read_csv(StringIO(data))
exp.replace("a", '"a', inplace=True)
tm.assert_frame_equal(df, exp)
