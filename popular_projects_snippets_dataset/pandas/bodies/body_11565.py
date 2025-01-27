# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
filename = datapath("io", "data", "xml", "baby_names.xml")
df_file = read_xml(filename, parser=parser, encoding="ISO-8859-1").head(5)

output = df_file.to_xml(encoding="ISO-8859-1", parser=parser)

if output is not None:
    # etree and lxml differ on quotes and case in xml declaration
    output = output.replace(
        '<?xml version="1.0" encoding="ISO-8859-1"?',
        "<?xml version='1.0' encoding='ISO-8859-1'?",
    )

assert output == encoding_expected
