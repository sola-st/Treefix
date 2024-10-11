# Extracted from https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-output-from-series-to-dataframe
 grouped=df.groupby(['Team','Year'])['W'].count().reset_index()

 team_wins_df=pd.DataFrame(grouped)
 team_wins_df=team_wins_df.rename({'W':'Wins'},axis=1)
 team_wins_df['Wins']=team_wins_df['Wins'].astype(np.int32)
 team_wins_df.reset_index()
 print(team_wins_df)

