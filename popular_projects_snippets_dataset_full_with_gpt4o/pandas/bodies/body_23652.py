# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""Write the file header"""
byteorder = self._byteorder
self._write_bytes(bytes("<stata_dta>", "utf-8"))
bio = BytesIO()
# ds_format - 117
bio.write(self._tag(bytes(str(self._dta_version), "utf-8"), "release"))
# byteorder
bio.write(self._tag(byteorder == ">" and "MSF" or "LSF", "byteorder"))
# number of vars, 2 bytes in 117 and 118, 4 byte in 119
nvar_type = "H" if self._dta_version <= 118 else "I"
bio.write(self._tag(struct.pack(byteorder + nvar_type, self.nvar), "K"))
# 117 uses 4 bytes, 118 uses 8
nobs_size = "I" if self._dta_version == 117 else "Q"
bio.write(self._tag(struct.pack(byteorder + nobs_size, self.nobs), "N"))
# data label 81 bytes, char, null terminated
label = data_label[:80] if data_label is not None else ""
encoded_label = label.encode(self._encoding)
label_size = "B" if self._dta_version == 117 else "H"
label_len = struct.pack(byteorder + label_size, len(encoded_label))
encoded_label = label_len + encoded_label
bio.write(self._tag(encoded_label, "label"))
# time stamp, 18 bytes, char, null terminated
# format dd Mon yyyy hh:mm
if time_stamp is None:
    time_stamp = datetime.datetime.now()
elif not isinstance(time_stamp, datetime.datetime):
    raise ValueError("time_stamp should be datetime type")
# Avoid locale-specific month conversion
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
month_lookup = {i + 1: month for i, month in enumerate(months)}
ts = (
    time_stamp.strftime("%d ")
    + month_lookup[time_stamp.month]
    + time_stamp.strftime(" %Y %H:%M")
)
# '\x11' added due to inspection of Stata file
stata_ts = b"\x11" + bytes(ts, "utf-8")
bio.write(self._tag(stata_ts, "timestamp"))
self._write_bytes(self._tag(bio.getvalue(), "header"))
