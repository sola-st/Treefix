# Extracted from https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value
  df = df.drop(df[df['line_race']==0].index)

