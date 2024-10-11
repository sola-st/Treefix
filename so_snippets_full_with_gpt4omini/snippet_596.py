# Extracted from https://stackoverflow.com/questions/14507794/how-to-flatten-a-hierarchical-index-in-columns
In [34]: df
Out[34]: 
     USAF   WBAN  day  month  s_CD  s_CL  s_CNT  s_PC  tempf         year
                               sum   sum    sum   sum   amax   amin      
0  702730  26451    1      1    12     0     13     1  30.92  24.98  1993
1  702730  26451    2      1    13     0     13     0  32.00  24.98  1993
2  702730  26451    3      1     2    10     13     1  23.00   6.98  1993
3  702730  26451    4      1    12     0     13     1  10.04   3.92  1993
4  702730  26451    5      1    10     0     13     3  19.94  10.94  1993


In [35]: mi = df.columns

In [36]: mi
Out[36]: 
MultiIndex
[(USAF, ), (WBAN, ), (day, ), (month, ), (s_CD, sum), (s_CL, sum), (s_CNT, sum), (s_PC, sum), (tempf, amax), (tempf, amin), (year, )]


In [37]: mi.tolist()
Out[37]: 
[('USAF', ''),
 ('WBAN', ''),
 ('day', ''),
 ('month', ''),
 ('s_CD', 'sum'),
 ('s_CL', 'sum'),
 ('s_CNT', 'sum'),
 ('s_PC', 'sum'),
 ('tempf', 'amax'),
 ('tempf', 'amin'),
 ('year', '')]

In [38]: ind = pd.Index([e[0] + e[1] for e in mi.tolist()])

In [39]: ind
Out[39]: Index([USAF, WBAN, day, month, s_CDsum, s_CLsum, s_CNTsum, s_PCsum, tempfamax, tempfamin, year], dtype=object)

In [40]: df.columns = ind




In [46]: df
Out[46]: 
     USAF   WBAN  day  month  s_CDsum  s_CLsum  s_CNTsum  s_PCsum  tempfamax  tempfamin  \
0  702730  26451    1      1       12        0        13        1      30.92      24.98   
1  702730  26451    2      1       13        0        13        0      32.00      24.98   
2  702730  26451    3      1        2       10        13        1      23.00       6.98   
3  702730  26451    4      1       12        0        13        1      10.04       3.92   
4  702730  26451    5      1       10        0        13        3      19.94      10.94   




   year  
0  1993  
1  1993  
2  1993  
3  1993  
4  1993

