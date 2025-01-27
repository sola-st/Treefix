# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
""" Convert headers to botocore keyword arguments.
        """
# This is required while we need to support both boto and botocore.
mapping = CaselessDict({
    'Content-Type': 'ContentType',
    'Cache-Control': 'CacheControl',
    'Content-Disposition': 'ContentDisposition',
    'Content-Encoding': 'ContentEncoding',
    'Content-Language': 'ContentLanguage',
    'Content-Length': 'ContentLength',
    'Content-MD5': 'ContentMD5',
    'Expires': 'Expires',
    'X-Amz-Grant-Full-Control': 'GrantFullControl',
    'X-Amz-Grant-Read': 'GrantRead',
    'X-Amz-Grant-Read-ACP': 'GrantReadACP',
    'X-Amz-Grant-Write-ACP': 'GrantWriteACP',
    'X-Amz-Object-Lock-Legal-Hold': 'ObjectLockLegalHoldStatus',
    'X-Amz-Object-Lock-Mode': 'ObjectLockMode',
    'X-Amz-Object-Lock-Retain-Until-Date': 'ObjectLockRetainUntilDate',
    'X-Amz-Request-Payer': 'RequestPayer',
    'X-Amz-Server-Side-Encryption': 'ServerSideEncryption',
    'X-Amz-Server-Side-Encryption-Aws-Kms-Key-Id': 'SSEKMSKeyId',
    'X-Amz-Server-Side-Encryption-Context': 'SSEKMSEncryptionContext',
    'X-Amz-Server-Side-Encryption-Customer-Algorithm': 'SSECustomerAlgorithm',
    'X-Amz-Server-Side-Encryption-Customer-Key': 'SSECustomerKey',
    'X-Amz-Server-Side-Encryption-Customer-Key-Md5': 'SSECustomerKeyMD5',
    'X-Amz-Storage-Class': 'StorageClass',
    'X-Amz-Tagging': 'Tagging',
    'X-Amz-Website-Redirect-Location': 'WebsiteRedirectLocation',
})
extra = {}
for key, value in headers.items():
    try:
        kwarg = mapping[key]
    except KeyError:
        raise TypeError(f'Header "{key}" is not supported by botocore')
    else:
        extra[kwarg] = value
exit(extra)
