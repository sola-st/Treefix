# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(KeyError, match=("doc is not included in namespaces")):

    geom_df.to_xml(
        namespaces={"": "http://example.com"}, prefix="doc", parser=parser
    )
