# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
expected = (
    "<?xml version='1.0' encoding='utf-8'?>\n"
    "<data><row><index>0</index><shape>square</shape>"
    "<degrees>360</degrees><sides>4.0</sides></row><row>"
    "<index>1</index><shape>circle</shape><degrees>360"
    "</degrees><sides/></row><row><index>2</index><shape>"
    "triangle</shape><degrees>180</degrees><sides>3.0</sides>"
    "</row></data>"
)

output = geom_df.to_xml(pretty_print=False, parser=parser)
output = equalize_decl(output)

# etree adds space for closed tags
if output is not None:
    output = output.replace(" />", "/>")

assert output == expected
