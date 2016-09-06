import nfldb
import pandas as pd
from fanduelvars import fanduel_point_conversions

"""
Helpers and convenience variables.
"""
all_weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
past_2_seasons = [2015,2016]
past_3_seasons = [2014].append(past_2_seasons)
past_4_seasons = [2013].append(past_3_seasons)
def sort_help(s):
	return s[3]



"""
Make a player matrix (DataFrame).
Rows = weeks
Colums = stats
"""
def player_matrix(name, year, weeks):     
    """
    Make a player matrix (DataFrame).
    Rows = weeks
    Columns = stats

    Step 1: Get stat categories relevant to player over the given time period (Cols)
    Step 2: Query all games in time period (get game objects), select those where the player played
    Step 3: Get player stats game by game, filling in categories/stats in empta data dict
    Step 4: Create #games x #categories dataframe
    """
    db = nfldb.connect()
    q = nfldb.Query(db)
    _labels  = q.player(full_name=name).as_aggregate()[0]
    _cols = list(_labels.fields)
    data = {}
    _index = []

    q.game(season_year=year, season_type='Regular', week=weeks)
    games = q.sort(('week', 'asc')).as_games()
    for i, g in enumerate(games):
        q = nfldb.Query(db).game(gsis_id=g.gsis_id)
        stats = q.player(full_name=name).as_aggregate()[0]

        for category in _cols:
	        if category not  in data:
	            data[category] = [getattr(stats, category, None)]
	        else:
	  	    data[category].append(getattr(stats, category, None))
        _index.append(str(g.season_year)+str(g.week))
    sorted_index = sorted(_index, key = sort_help)
    frame = pd.DataFrame(data=data, index=sorted_index)
     

    """
    Make a unique Fantasy Points Scoring Vector for this player.
    """

    cooper_vector_data = {}

    for k,v in fanduel_point_conversions.iteritems():
        if k in _cols:
            cooper_vector_data[k]=v


    cooper_vector = pd.Series(cooper_vector_data)
    cooper_vector = frame.dot(cooper_vector)
    frame['fantasy_points']=cooper_vector
    return frame
