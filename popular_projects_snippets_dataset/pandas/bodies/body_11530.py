# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml = "https://www.w3schools.com/xml/cdcatalog_with_xsl.xml"
xsl = "https://www.w3schools.com/xml/cdcatalog.xsl"

df_xsl = read_xml(
    xml,
    xpath=".//tr[td and position() <= 6]",
    names=["title", "artist"],
    stylesheet=xsl,
)

df_expected = DataFrame(
    {
        "title": {
            0: "Empire Burlesque",
            1: "Hide your heart",
            2: "Greatest Hits",
            3: "Still got the blues",
            4: "Eros",
        },
        "artist": {
            0: "Bob Dylan",
            1: "Bonnie Tyler",
            2: "Dolly Parton",
            3: "Gary Moore",
            4: "Eros Ramazzotti",
        },
    }
)

tm.assert_frame_equal(df_expected, df_xsl)
