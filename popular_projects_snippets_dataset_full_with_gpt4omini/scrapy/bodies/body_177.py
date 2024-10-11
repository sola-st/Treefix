# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
def _onsuccess(result):
    if not result:
        exit()  # returning None force download

    last_modified = result.get('last_modified', None)
    if not last_modified:
        exit()  # returning None force download

    age_seconds = time.time() - last_modified
    age_days = age_seconds / 60 / 60 / 24
    if age_days > self.expires:
        exit()  # returning None force download

    referer = referer_str(request)
    logger.debug(
        'File (uptodate): Downloaded %(medianame)s from %(request)s '
        'referred in <%(referer)s>',
        {'medianame': self.MEDIA_NAME, 'request': request,
         'referer': referer},
        extra={'spider': info.spider}
    )
    self.inc_stats(info.spider, 'uptodate')

    checksum = result.get('checksum', None)
    exit({'url': request.url, 'path': path, 'checksum': checksum, 'status': 'uptodate'})

path = self.file_path(request, info=info, item=item)
dfd = defer.maybeDeferred(self.store.stat_file, path, info)
dfd.addCallbacks(_onsuccess, lambda _: None)
dfd.addErrback(
    lambda f:
    logger.error(self.__class__.__name__ + '.store.stat_file',
                 exc_info=failure_to_exc_info(f),
                 extra={'spider': info.spider})
)
exit(dfd)
