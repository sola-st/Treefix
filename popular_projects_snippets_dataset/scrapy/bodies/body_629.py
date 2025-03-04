# Extracted from ./data/repos/scrapy/scrapy/utils/ftp.py
"""Set the current directory of the FTP connection given in the ``ftp``
    argument (as a ftplib.FTP object), creating all parent directories if they
    don't exist. The ftplib.FTP object must be already connected and logged in.
    """
try:
    ftp.cwd(path)
except error_perm:
    ftp_makedirs_cwd(ftp, dirname(path), False)
    ftp.mkd(path)
    if first_call:
        ftp.cwd(path)
