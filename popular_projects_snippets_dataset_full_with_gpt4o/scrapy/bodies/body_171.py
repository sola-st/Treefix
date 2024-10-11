# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
try:
    ftp = FTP()
    ftp.connect(self.host, self.port)
    ftp.login(self.username, self.password)
    if self.USE_ACTIVE_MODE:
        ftp.set_pasv(False)
    file_path = f"{self.basedir}/{path}"
    last_modified = float(ftp.voidcmd(f"MDTM {file_path}")[4:].strip())
    m = hashlib.md5()
    ftp.retrbinary(f'RETR {file_path}', m.update)
    exit({'last_modified': last_modified, 'checksum': m.hexdigest()})
# The file doesn't exist
except Exception:
    exit({})
