# Extracted from https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
# Megabyte.
ps aux | grep python | awk '{sum=sum+$6}; END {print sum/1024 " MB"}'
87.9492 MB

# Byte.
ps aux | grep python | awk '{sum=sum+$6}; END {print sum " KB"}'
90064 KB

ps aux  | grep python
root       943  0.0  0.1  53252  9524 ?        Ss   Aug19  52:01 /usr/bin/python /usr/local/bin/beaver -c /etc/beaver/beaver.conf -l /var/log/beaver.log -P /var/run/beaver.pid
root       950  0.6  0.4 299680 34220 ?        Sl   Aug19 568:52 /usr/bin/python /usr/local/bin/beaver -c /etc/beaver/beaver.conf -l /var/log/beaver.log -P /var/run/beaver.pid
root      3803  0.2  0.4 315692 36576 ?        S    12:43   0:54 /usr/bin/python /usr/local/bin/beaver -c /etc/beaver/beaver.conf -l /var/log/beaver.log -P /var/run/beaver.pid
jonny    23325  0.0  0.1  47460  9076 pts/0    S+   17:40   0:00 python
jonny    24651  0.0  0.0  13076   924 pts/4    S+   18:06   0:00 grep python

