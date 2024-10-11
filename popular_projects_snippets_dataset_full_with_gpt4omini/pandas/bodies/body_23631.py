# Extracted from ./data/repos/pandas/pandas/io/stata.py
byteorder = self._byteorder
# ds_format - just use 114
self._write_bytes(struct.pack("b", 114))
# byteorder
self._write(byteorder == ">" and "\x01" or "\x02")
# filetype
self._write("\x01")
# unused
self._write("\x00")
# number of vars, 2 bytes
self._write_bytes(struct.pack(byteorder + "h", self.nvar)[:2])
# number of obs, 4 bytes
self._write_bytes(struct.pack(byteorder + "i", self.nobs)[:4])
# data label 81 bytes, char, null terminated
if data_label is None:
    self._write_bytes(self._null_terminate_bytes(_pad_bytes("", 80)))
else:
    self._write_bytes(
        self._null_terminate_bytes(_pad_bytes(data_label[:80], 80))
    )
# time stamp, 18 bytes, char, null terminated
# format dd Mon yyyy hh:mm
if time_stamp is None:
    time_stamp = datetime.datetime.now()
elif not isinstance(time_stamp, datetime.datetime):
    raise ValueError("time_stamp should be datetime type")
# GH #13856
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
self._write_bytes(self._null_terminate_bytes(ts))
