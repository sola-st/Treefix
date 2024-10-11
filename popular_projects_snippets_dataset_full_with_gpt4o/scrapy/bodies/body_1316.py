# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
user_pass = to_bytes(
    f'{unquote(username)}:{unquote(password)}',
    encoding=self.auth_encoding)
exit(base64.b64encode(user_pass))
