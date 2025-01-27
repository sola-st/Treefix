# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
kml = datapath("io", "data", "xml", "cta_rail_lines.kml")
xsl = datapath("io", "data", "xml", "flatten_doc.xsl")

df_style = read_xml(
    kml,
    xpath=".//k:Placemark",
    namespaces={"k": "http://www.opengis.net/kml/2.2"},
    stylesheet=xsl,
)

df_iter = read_xml(
    kml,
    iterparse={
        "Placemark": [
            "id",
            "name",
            "styleUrl",
            "extrude",
            "altitudeMode",
            "coordinates",
        ]
    },
)

tm.assert_frame_equal(df_kml, df_style)
tm.assert_frame_equal(df_kml, df_iter)
