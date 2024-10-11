# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
# Python Software Foundation (2019 IRS-990 RETURN)
s3 = "s3://irs-form-990/201923199349319487_public.xml"

df_lxml = read_xml(
    s3,
    xpath=".//irs:Form990PartVIISectionAGrp",
    namespaces={"irs": "http://www.irs.gov/efile"},
    parser="lxml",
    storage_options={"anon": True},
)

df_etree = read_xml(
    s3,
    xpath=".//irs:Form990PartVIISectionAGrp",
    namespaces={"irs": "http://www.irs.gov/efile"},
    parser="etree",
    storage_options={"anon": True},
)

tm.assert_frame_equal(df_lxml, df_etree)
