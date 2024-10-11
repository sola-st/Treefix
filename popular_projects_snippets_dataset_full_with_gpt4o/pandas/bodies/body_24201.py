# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
self.filepath_or_buffer.seek(0)

# read file header
line1 = self._get_row()
if line1 != _correct_line1:
    if "**COMPRESSED**" in line1:
        # this was created with the PROC CPORT method and can't be read
        # https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/movefile/p1bm6aqp3fw4uin1hucwh718f6kp.htm
        raise ValueError(
            "Header record indicates a CPORT file, which is not readable."
        )
    raise ValueError("Header record is not an XPORT file.")

line2 = self._get_row()
fif = [["prefix", 24], ["version", 8], ["OS", 8], ["_", 24], ["created", 16]]
file_info = _split_line(line2, fif)
if file_info["prefix"] != "SAS     SAS     SASLIB":
    raise ValueError("Header record has invalid prefix.")
file_info["created"] = _parse_date(file_info["created"])
self.file_info = file_info

line3 = self._get_row()
file_info["modified"] = _parse_date(line3[:16])

# read member header
header1 = self._get_row()
header2 = self._get_row()
headflag1 = header1.startswith(_correct_header1)
headflag2 = header2 == _correct_header2
if not (headflag1 and headflag2):
    raise ValueError("Member header not found")
# usually 140, could be 135
fieldnamelength = int(header1[-5:-2])

# member info
mem = [
    ["prefix", 8],
    ["set_name", 8],
    ["sasdata", 8],
    ["version", 8],
    ["OS", 8],
    ["_", 24],
    ["created", 16],
]
member_info = _split_line(self._get_row(), mem)
mem = [["modified", 16], ["_", 16], ["label", 40], ["type", 8]]
member_info.update(_split_line(self._get_row(), mem))
member_info["modified"] = _parse_date(member_info["modified"])
member_info["created"] = _parse_date(member_info["created"])
self.member_info = member_info

# read field names
types = {1: "numeric", 2: "char"}
fieldcount = int(self._get_row()[54:58])
datalength = fieldnamelength * fieldcount
# round up to nearest 80
if datalength % 80:
    datalength += 80 - datalength % 80
fielddata = self.filepath_or_buffer.read(datalength)
fields = []
obs_length = 0
while len(fielddata) >= fieldnamelength:
    # pull data for one field
    fieldbytes, fielddata = (
        fielddata[:fieldnamelength],
        fielddata[fieldnamelength:],
    )

    # rest at end gets ignored, so if field is short, pad out
    # to match struct pattern below
    fieldbytes = fieldbytes.ljust(140)

    fieldstruct = struct.unpack(">hhhh8s40s8shhh2s8shhl52s", fieldbytes)
    field = dict(zip(_fieldkeys, fieldstruct))
    del field["_"]
    field["ntype"] = types[field["ntype"]]
    fl = field["field_length"]
    if field["ntype"] == "numeric" and ((fl < 2) or (fl > 8)):
        msg = f"Floating field width {fl} is not between 2 and 8."
        raise TypeError(msg)

    for k, v in field.items():
        try:
            field[k] = v.strip()
        except AttributeError:
            pass

    obs_length += field["field_length"]
    fields += [field]

header = self._get_row()
if not header == _correct_obs_header:
    raise ValueError("Observation header not found.")

self.fields = fields
self.record_length = obs_length
self.record_start = self.filepath_or_buffer.tell()

self.nobs = self._record_count()
self.columns = [x["name"].decode() for x in self.fields]

# Setup the dtype.
dtypel = [
    ("s" + str(i), "S" + str(field["field_length"]))
    for i, field in enumerate(self.fields)
]
dtype = np.dtype(dtypel)
self._dtype = dtype
