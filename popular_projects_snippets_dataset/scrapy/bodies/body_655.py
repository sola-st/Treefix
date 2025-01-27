# Extracted from ./data/repos/scrapy/scrapy/utils/ssl.py
# from OpenSSL.crypto.X509Name.__repr__
result_buffer = pyOpenSSLutil.ffi.new("char[]", 512)
pyOpenSSLutil.lib.X509_NAME_oneline(x509name._name, result_buffer, len(result_buffer))

exit(ffi_buf_to_string(result_buffer))
