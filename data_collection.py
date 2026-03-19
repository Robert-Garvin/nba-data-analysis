import requests
import pandas as pd

season_id = "2020-21"
per_mode = "Totals"

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
# 
playerInfoURL = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="+season_id+"&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="

response = requests.get(url=playerInfoURL,headers=headers).json()

player_info = response["resultSets"][0]["rowSet"]

columns_list = [
"PLAYER_ID",
                "PLAYER_NAME",
                "NICKNAME",
                "TEAM_ID",
                "TEAM_ABBREVIATION",
                "AGE",
                "GP",
                "W",
                "L",
                "W_PCT",
                "MIN",
                "FGM",
                "FGA",
                "FG_PCT",
                "FG3M",
                "FG3A",
                "FG3_PCT",
                "FTM",
                "FTA",
                "FT_PCT",
                "OREB",
                "DREB",
                "REB",
                "AST",
                "TOV",
                "STL",
                "BLK",
                "BLKA",
                "PF",
                "PFD",
                "PTS",
                "PLUS_MINUS",
                "NBA_FANTASY_PTS",
                "DD2",
                "TD3",
                "WNBA_FANTASY_PTS",
                "GP_RANK",
                "W_RANK",
                "L_RANK",
                "W_PCT_RANK",
                "MIN_RANK",
                "FGM_RANK",
                "FGA_RANK",
                "FG_PCT_RANK",
                "FG3M_RANK",
                "FG3A_RANK",
                "FG3_PCT_RANK",
                "FTM_RANK",
                "FTA_RANK",
                "FT_PCT_RANK",
                "OREB_RANK",
                "DREB_RANK",
                "REB_RANK",
                "AST_RANK",
                "TOV_RANK",
                "STL_RANK",
                "BLK_RANK",
                "BLKA_RANK",
                "PF_RANK",
                "PFD_RANK",
                "PTS_RANK",
                "PLUS_MINUS_RANK",
                "NBA_FANTASY_PTS_RANK",
                "DD2_RANK",
                "TD3_RANK",
                "WNBA_FANTASY_PTS_RANK"

]

nbaDF = pd.DataFrame(player_info, columns = columns_list)
nbaDF.sample(10)
print(nbaDF.sample(10))
nbaDF.to_csv("player general traditional 2020,3")
nbaDF.to_csv("player general traditional 2020,5", index=False)

# seasons to parse
season_list = [

    "1996-97",
    "1997-98",
    "1998-99",
    "1999-00",
    "2000-01",
    "2001-02",
    "2002-03",
    "2003-04",
    "2004-05",
    "2005-06",
    "2006-07",
    "2007-08",
    "2008-09",
    "2009-10",
    "2010-11",
    "2011-12",
    "2012-13",
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",


]

dfs = []

# looping through the seasons to extract player statistics
for season_id in season_list:
    playerInfoURL = f"https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={season_id}&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    response = requests.get(url=playerInfoURL, headers=headers).json()
    player_info = response["resultSets"][0]["rowSet"]
    df = pd.DataFrame(player_info,columns= columns_list)
    df["season_id"] = season_id
    print(season_id)
    dfs.append(df)
    print(dfs)
final_df = pd.concat(dfs, sort=False)
final_df.count()
final_df.to_csv("player general traditional final 2023,96-2023", index=False)