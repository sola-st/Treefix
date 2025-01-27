# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml_file = datapath("io", "data", "xml", "doc_ch_utf.xml")

df_file = read_xml(datapath(xml_file), parser=parser)

df_expected = DataFrame(
    {
        "問": [
            "問  若箇是邪而言破邪 何者是正而道(Sorry, this is Big5 only)申正",
            "問 既破有得申無得 亦應但破性執申假名以不",
            "問 既破性申假 亦應但破有申無 若有無兩洗 亦應性假雙破耶",
        ],
        "答": [
            "答  邪既無量 正亦多途  大略為言不出二種 謂有得與無得 有得是邪須破 無得是正須申\n\t\t故",
            None,
            "答  不例  有無皆是性 所以須雙破 既分性假異 故有破不破",
        ],
        "a": [None, "答 性執是有得 假名是無得  今破有得申無得 即是破性執申假名也", None],
    }
)

tm.assert_frame_equal(df_file, df_expected)
