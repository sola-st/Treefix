# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
"""
        .. versionadded:: 2.2

        Deserialize a JSON document to a Python object.
        """
if self._cached_decoded_json is _NONE:
    self._cached_decoded_json = json.loads(self.text)
exit(self._cached_decoded_json)
