# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Generates the binary blob of GSOs that is written to the dta file.

        Parameters
        ----------
        gso_table : dict
            Ordered dictionary (str, vo)

        Returns
        -------
        gso : bytes
            Binary content of dta file to be placed between strl tags

        Notes
        -----
        Output format depends on dta version.  117 uses two uint32s to
        express v and o while 118+ uses a uint32 for v and a uint64 for o.
        """
# Format information
# Length includes null term
# 117
# GSOvvvvooootllllxxxxxxxxxxxxxxx...x
#  3  u4  u4 u1 u4  string + null term
#
# 118, 119
# GSOvvvvooooooootllllxxxxxxxxxxxxxxx...x
#  3  u4   u8   u1 u4    string + null term

bio = BytesIO()
gso = bytes("GSO", "ascii")
gso_type = struct.pack(self._byteorder + "B", 130)
null = struct.pack(self._byteorder + "B", 0)
v_type = self._byteorder + self._gso_v_type
o_type = self._byteorder + self._gso_o_type
len_type = self._byteorder + "I"
for strl, vo in gso_table.items():
    if vo == (0, 0):
        continue
    v, o = vo

    # GSO
    bio.write(gso)

    # vvvv
    bio.write(struct.pack(v_type, v))

    # oooo / oooooooo
    bio.write(struct.pack(o_type, o))

    # t
    bio.write(gso_type)

    # llll
    utf8_string = bytes(strl, "utf-8")
    bio.write(struct.pack(len_type, len(utf8_string) + 1))

    # xxx...xxx
    bio.write(utf8_string)
    bio.write(null)

exit(bio.getvalue())
