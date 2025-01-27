# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
bad_xml = """\
<?xml version='1.0' encoding='utf-8'?>
  <row>
    <shape>square</shape>
    <degrees>00360</degrees>
    <sides>4.0</sides>
    <date>2020-01-01</date>
   </row>
  <row>
    <shape>circle</shape>
    <degrees>00360</degrees>
    <sides/>
    <date>2021-01-01</date>
  </row>
  <row>
    <shape>triangle</shape>
    <degrees>00180</degrees>
    <sides>3.0</sides>
    <date>2022-01-01</date>
  </row>
"""
with tm.ensure_clean(filename="bad.xml") as path:
    with open(path, "w") as f:
        f.write(bad_xml)

    with pytest.raises(
        SyntaxError,
        match=(
            "Extra content at the end of the document|"
            "junk after document element"
        ),
    ):
        read_xml(
            path,
            parser=parser,
            parse_dates=["date"],
            iterparse={"row": ["shape", "degrees", "sides", "date"]},
        )
