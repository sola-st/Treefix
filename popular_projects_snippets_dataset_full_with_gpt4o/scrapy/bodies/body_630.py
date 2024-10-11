# Extracted from ./data/repos/scrapy/scrapy/utils/ftp.py
"""Opens a FTP connection with passed credentials,sets current directory
    to the directory extracted from given path, then uploads the file to server
    """
with FTP() as ftp:
    ftp.connect(host, port)
    ftp.login(username, password)
    if use_active_mode:
        ftp.set_pasv(False)
    file.seek(0)
    dirname, filename = posixpath.split(path)
    ftp_makedirs_cwd(ftp, dirname)
    command = 'STOR' if overwrite else 'APPE'
    ftp.storbinary(f'{command} {filename}', file)
    file.close()
