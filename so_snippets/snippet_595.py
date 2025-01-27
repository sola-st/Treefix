# Extracted from https://stackoverflow.com/questions/34962104/how-can-i-use-the-apply-function-for-a-single-column
   a  b
0  1  2
1  2  3
2  3  4
3  4  5

df['a'] = df['a'].apply(lambda x: x + 1)

   a  b
0  2  2
1  3  3
2  4  4
3  5  5

