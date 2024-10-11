# Extracted from https://stackoverflow.com/questions/31237042/whats-the-difference-between-select-related-and-prefetch-related-in-django-orm
SELECT "credential"."id",
       "credential"."uuid",
       "credential"."identity_id"
FROM   "credential"
WHERE  "credential"."identity_id" IN
    (84706, 48746, 871441, 84713, 76492, 84621, 51472);

