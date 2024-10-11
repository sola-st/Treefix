from ftplib import FTP # pragma: no cover
from os.path import split # pragma: no cover

host = 'localhost' # pragma: no cover
port = 21 # pragma: no cover
username = 'user' # pragma: no cover
password = 'pass' # pragma: no cover
use_active_mode = False # pragma: no cover
path = '/test/path/to/file.txt' # pragma: no cover
class MockFTP: # pragma: no cover
    def connect(self, host, port): # pragma: no cover
        pass # pragma: no cover
    def login(self, username, password): # pragma: no cover
        pass # pragma: no cover
    def set_pasv(self, val): # pragma: no cover
        pass # pragma: no cover
    def retrbinary(self, cmd, callback): # pragma: no cover
        callback(b'test data') # pragma: no cover
    def cwd(self, dirname): # pragma: no cover
        pass # pragma: no cover
    def delete(self, filename): # pragma: no cover
        print('Deleted file:', filename) # pragma: no cover
        exec('# uncovered') # pragma: no cover
FTP = MockFTP # pragma: no cover
exit = print # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
from l3.Runtime import _l_
try:
    from ftplib import FTP
    _l_(16365)

except ImportError:
    pass
ftp = FTP()
_l_(16366)
ftp.connect(host, port)
_l_(16367)
ftp.login(username, password)
_l_(16368)
if use_active_mode:
    _l_(16370)

    ftp.set_pasv(False)
    _l_(16369)
ftp_data = []
_l_(16371)

def buffer_data(data):
    _l_(16373)

    ftp_data.append(data)
    _l_(16372)
ftp.retrbinary(f'RETR {path}', buffer_data)
_l_(16374)
dirname, filename = split(path)
_l_(16375)
ftp.cwd(dirname)
_l_(16376)
ftp.delete(filename)
_l_(16377)
aux = "".join(ftp_data)
_l_(16378)
exit(aux)
