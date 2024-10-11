# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
url = (
    "https://data.cityofchicago.org/api/views/"
    "8pix-ypme/rows.xml?accessType=DOWNLOAD"
)

with tm.ensure_clean(filename="cta.xml") as path:
    (read_xml(url, xpath=".//row/row", parser=parser).to_xml(path, index=False))

    df_xpath = read_xml(path, parser=parser)
    df_iter = read_xml(
        path,
        parser=parser,
        iterparse={
            "row": [
                "_id",
                "_uuid",
                "_position",
                "_address",
                "stop_id",
                "direction_id",
                "stop_name",
                "station_name",
                "station_descriptive_name",
                "map_id",
                "ada",
                "red",
                "blue",
                "g",
                "brn",
                "p",
                "pexp",
                "y",
                "pnk",
                "o",
                "location",
            ]
        },
    )

tm.assert_frame_equal(df_xpath, df_iter)
