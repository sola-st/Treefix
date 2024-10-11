# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
unicode_df = self.read_dta(datapath("io", "data", "stata", "stata16_118.dta"))

columns = ["utf8", "latin1", "ascii", "utf8_strl", "ascii_strl"]
values = [
    ["ραηδας", "PÄNDÄS", "p", "ραηδας", "p"],
    ["ƤĀńĐąŜ", "Ö", "a", "ƤĀńĐąŜ", "a"],
    ["ᴘᴀᴎᴅᴀS", "Ü", "n", "ᴘᴀᴎᴅᴀS", "n"],
    ["      ", "      ", "d", "      ", "d"],
    [" ", "", "a", " ", "a"],
    ["", "", "s", "", "s"],
    ["", "", " ", "", " "],
]
expected = DataFrame(values, columns=columns)

tm.assert_frame_equal(unicode_df, expected)
