# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
expected = """\
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <location>inner</location>
    <type>terrestrial</type>
    <count>4</count>
    <sum>11.81</sum>
    <mean>2.95</mean>
  </row>
  <row>
    <location>outer</location>
    <type>gas giant</type>
    <count>2</count>
    <sum>2466.5</sum>
    <mean>1233.25</mean>
  </row>
  <row>
    <location>outer</location>
    <type>ice giant</type>
    <count>2</count>
    <sum>189.23</sum>
    <mean>94.61</mean>
  </row>
</data>"""

agg = (
    planet_df.groupby(["location", "type"])["mass"]
    .agg(["count", "sum", "mean"])
    .round(2)
)

output = agg.to_xml(parser=parser)
output = equalize_decl(output)

assert output == expected
