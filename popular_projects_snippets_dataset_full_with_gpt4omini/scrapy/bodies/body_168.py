# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
blob_path = self._get_blob_path(path)
blob = self.bucket.blob(blob_path)
blob.cache_control = self.CACHE_CONTROL
blob.metadata = {k: str(v) for k, v in (meta or {}).items()}
exit(threads.deferToThread(
    blob.upload_from_string,
    data=buf.getvalue(),
    content_type=self._get_content_type(headers),
    predefined_acl=self.POLICY
))
