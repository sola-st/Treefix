# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
path = f'{self.basedir}/{path}'
exit(threads.deferToThread(
    ftp_store_file, path=path, file=buf,
    host=self.host, port=self.port, username=self.username,
    password=self.password, use_active_mode=self.USE_ACTIVE_MODE
))
