import nfldb
db = nfldb.connect()


q = nfldb.Query(db)

q.game(season_year=2012, season_type='Regular')
for play in q.sort(('passing_yds','asc')).limit(5).as_plays():
	print play
