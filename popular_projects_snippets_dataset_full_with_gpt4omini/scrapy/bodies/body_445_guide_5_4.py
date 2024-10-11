from ftplib import FTP # pragma: no cover
from os.path import split # pragma: no cover

host = 'localhost' # pragma: no cover
port = 21 # pragma: no cover
username = 'user' # pragma: no cover
password = 'password' # pragma: no cover
use_active_mode = True # pragma: no cover
path = 'files/test_file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
from l3.Runtime import _l_
try:
    from ftplib import FTP
    _l_(5207)

except ImportError:
    pass
ftp = FTP()
_l_(5208)
ftp.connect(host, port)
_l_(5209)
ftp.login(username, password)
_l_(5210)
if use_active_mode:
    _l_(5212)

    ftp.set_pasv(False)
    _l_(5211)
ftp_data = []
_l_(5213)

def buffer_data(data):
    _l_(5215)

    ftp_data.append(data)
    _l_(5214)
ftp.retrbinary(f'RETR {path}', buffer_data)
_l_(5216)
dirname, filename = split(path)
_l_(5217)
ftp.cwd(dirname)
_l_(5218)
ftp.delete(filename)
_l_(5219)
aux = "".join(ftp_data)
_l_(5220)
exit(aux)
