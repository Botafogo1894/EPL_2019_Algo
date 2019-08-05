# api.football-data.org/v2/competitions/PL/standings
import http.client
import requests
import json

url1 = 'api.football-data.org'

def get_table(url1):
    connection = http.client.HTTPConnection(url1)
    headers = { 'X-Auth-Token': '2a9a431414744c4a87048d64b726442f' }
    connection.request('GET', '/v2/competitions/PL/standings', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    return response

def final_teams_list(url1):
    return get_table(url1)['standings'][0]['table']

test = final_teams_list(url1)


# TABLE SCRAPE
# 'team': {'id': 57, 'name': 'Arsenal FC',
# 'team': {'id': 58, 'name': 'Aston Villa FC',
# 'team': {'id': 1044, 'name': 'AFC Bournemouth'
# 'team': {'id': 397, 'name': 'Brighton & Hove Albion FC',
# 'team': {'id': 328, 'name': 'Burnley FC',
# 'team': {'id': 61, 'name': 'Chelsea FC',
# 'team': {'id': 354, 'name': 'Crystal Palace FC',
# 'team': {'id': 62, 'name': 'Everton FC',
# 'team': {'id': 338, 'name': 'Leicester City FC',
# 'team': {'id': 64, 'name': 'Liverpool FC',
# 'team': {'id': 65, 'name': 'Manchester City FC',
# 'team': {'id': 67, 'name': 'Newcastle United FC',
# 'team': {'id': 66, 'name': 'Manchester United FC',
# 'team': {'id': 68, 'name': 'Norwich City FC',
# 'team': {'id': 356, 'name': 'Sheffield United FC',
# 'team': {'id': 340, 'name': 'Southampton FC',
# 'team': {'id': 73, 'name': 'Tottenham Hotspur FC',
# 'team': {'id': 346, 'name': 'Watford FC',
# 'team': {'id': 563, 'name': 'West Ham United FC',
# 'team': {'id': 76, 'name': 'Wolverhampton Wanderers FC',



# PLAYERS SCRAPE
# 'code': 3, 'id': 1, 'name': 'Arsenal FC',  'short_name': 'ARS',
# 'code': 7, 'id': 2, 'name': 'Aston Villa',  'short_name': 'AVL',
# 'code': 91, 'id': 3, 'name': 'AFC Bournemouth',  'short_name': 'BOU',
# 'code': 36, 'id': 4, 'name': 'Brighton & Hove Albion FC',  'short_name': 'BHA',
# 'code': 90, 'id': 5, 'name': 'Burnley FC',  'short_name': 'BUR',
# 'code': 8, 'id': 6, 'name': 'Chelsea FC',  'short_name': 'CHE',
# 'code': 31, 'id': 7, 'name': 'Crystal Palace FC',  'short_name': 'CRY',
# 'code': 11, 'id': 8, 'name': 'Everton FC',  'short_name': 'EVE',
# 'code': 13, 'id': 9, 'name': 'Leicester City FC',  'short_name': 'LEI',
# 'code': 14, 'id': 10, 'name': 'Liverpool FC',  'short_name': 'LIV',
# 'code': 43, 'id': 11, 'name': 'Manchester City FC',  'short_name': 'MCI',
# 'code': 1, 'id': 12, 'name': 'Manchester United FC',  'short_name': 'MUN',
# 'code': 4, 'id': 13, 'name': 'Newcastle United FC',  'short_name': 'NEW',
# 'code': 45, 'id': 14, 'name': 'Norwich',  'short_name': 'NOR',
# 'code': 49, 'id': 15, 'name': 'Sheffield Utd',  'short_name': 'SHU',
# 'code': 20, 'id': 16, 'name': 'Southampton FC',  'short_name': 'SOU',
# 'code': 6, 'id': 17, 'name': 'Tottenham Hotspur FC',  'short_name': 'TOT',
# 'code': 57, 'id': 18, 'name': 'Watford FC',  'short_name': 'WAT',
# 'code': 21, 'id': 19, 'name': 'West Ham United FC',  'short_name': 'WHU',
# 'code': 39, 'id': 20, 'name': 'Wolverhampton Wanderers FC',  'short_name': 'WOL'



# [

# {'code': 3, 'draw': 0, 'form': None, 'id': 1, 'loss': 0,  'me': 'Arsenal FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'ARS', 'strength': 4, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1250, 'strength_overall_away': 1330, 'strength_attack_home': 1240, 'strength_attack_away': 1270, 'strength_defence_home': 1290, 'strength_defence_away': 1330},

# {'code': 7, 'draw': 0, 'form': None, 'id': 2, 'loss': 0, 'me': 'Aston Villa FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'AVL', 'strength': 2, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 990, 'strength_overall_away': 1050, 'strength_attack_home': 1050, 'strength_attack_away': 1050, 'strength_defence_home': 1030, 'strength_defence_away': 1070},

# {'code': 91, 'draw': 0, 'form': None, 'id': 3, 'loss': 0, 'me': 'AFC Bournemouth', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'BOU', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1050, 'strength_overall_away': 1140, 'strength_attack_home': 1040, 'strength_attack_away': 1100, 'strength_defence_home': 1120, 'strength_defence_away': 1170},

# {'code': 36, 'draw': 0, 'form': None, 'id': 4, 'loss': 0, 'me': 'Brighton & Hove Albion FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'BHA', 'strength': 2, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1000, 'strength_overall_away': 1070, 'strength_attack_home': 1040, 'strength_attack_away': 1140, 'strength_defence_home': 1050, 'strength_defence_away': 1070},

# {'code': 90, 'draw': 0, 'form': None, 'id': 5, 'loss': 0, 'me': 'Burnley FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'BUR', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1070, 'strength_overall_away': 1090, 'strength_attack_home': 990, 'strength_attack_away': 1030, 'strength_defence_home': 1060, 'strength_defence_away': 1070},

# {'code': 8, 'draw': 0, 'form': None, 'id': 6, 'loss': 0, 'me': 'Chelsea FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'CHE', 'strength': 4, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1280, 'strength_overall_away': 1310, 'strength_attack_home': 1270, 'strength_attack_away': 1340, 'strength_defence_home': 1280, 'strength_defence_away': 1330},

# {'code': 31, 'draw': 0, 'form': None, 'id': 7, 'loss': 0, 'me': 'Crystal Palace FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'CRY', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1130, 'strength_overall_away': 1080, 'strength_attack_home': 1030, 'strength_attack_away': 1180, 'strength_defence_home': 1100, 'strength_defence_away': 1070},

# {'code': 11, 'draw': 0, 'form': None, 'id': 8, 'loss': 0, 'me': 'Everton FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'EVE', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1100, 'strength_overall_away': 1220, 'strength_attack_home': 1070, 'strength_attack_away': 1120, 'strength_defence_home': 1120, 'strength_defence_away': 1210},

# {'code': 13, 'draw': 0, 'form': None, 'id': 9, 'loss': 0, 'me': 'Leicester City FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'LEI', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1110, 'strength_overall_away': 1120, 'strength_attack_home': 1130, 'strength_attack_away': 1180, 'strength_defence_home': 1110, 'strength_defence_away': 1110},

# {'code': 14, 'draw': 0, 'form': None, 'id': 10, 'loss': 0,  ame': 'Liverpool FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'LIV', 'strength': 5, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1340, 'strength_overall_away': 1350, 'strength_attack_home': 1330, 'strength_attack_away': 1360, 'strength_defence_home': 1330, 'strength_defence_away': 1360},

# {'code': 43, 'draw': 0, 'form': None, 'id': 11, 'loss': 0,  name': 'Manchester City FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'MCI', 'strength': 5, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1340, 'strength_overall_away': 1360, 'strength_attack_home': 1320, 'strength_attack_away': 1330, 'strength_defence_home': 1340, 'strength_defence_away': 1370},

# {'code': 1, 'draw': 0, 'form': None, 'id': 12, 'loss': 0,  'name': 'Manchester United FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'MUN', 'strength': 4, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1310, 'strength_overall_away': 1330, 'strength_attack_home': 1250, 'strength_attack_away': 1260, 'strength_defence_home': 1310, 'strength_defence_away': 1340},

# {'code': 4, 'draw': 0, 'form': None, 'id': 13, 'loss': 0,   'name': 'Newcastle United FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'NEW', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1080, 'strength_overall_away': 1110, 'strength_attack_home': 1070, 'strength_attack_away': 1110, 'strength_defence_home': 1070, 'strength_defence_away': 1090},

# {'code': 45, 'draw': 0, 'form': None, 'id': 14, 'loss': 0,    'name': 'Norwich City FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'NOR', 'strength': 2, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 990, 'strength_overall_away': 1060, 'strength_attack_home': 1050, 'strength_attack_away': 1050, 'strength_defence_home': 1060, 'strength_defence_away': 1080}, 

# {'code': 49, 'draw': 0, 'form': None, 'id': 15, 'loss': 0,     'name': 'Sheffield United FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'SHU', 'strength': 2, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 990, 'strength_overall_away': 1060, 'strength_attack_home': 1060, 'strength_attack_away': 1080, 'strength_defence_home': 1030, 'strength_defence_away': 1050},

# {'code': 20, 'draw': 0, 'form': None, 'id': 16, 'loss': 0,      'name': 'Southampton FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'SOU', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1060, 'strength_overall_away': 1090, 'strength_attack_home': 1040, 'strength_attack_away': 1070, 'strength_defence_home': 1100, 'strength_defence_away': 1110},

# {'code': 6, 'draw': 0, 'form': None, 'id': 17, 'loss': 0,       'name': 'Tottenham Hotspur FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'TOT', 'strength': 4, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1320, 'strength_overall_away': 1310, 'strength_attack_home': 1270, 'strength_attack_away': 1340, 'strength_defence_home': 1320, 'strength_defence_away': 1330},

# {'code': 57, 'draw': 0, 'form': None, 'id': 18, 'loss': 0,        'name': 'Watford FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'WAT', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1110, 'strength_overall_away': 1110, 'strength_attack_home': 1100, 'strength_attack_away': 1100, 'strength_defence_home': 1110, 'strength_defence_away': 1120},

# {'code': 21, 'draw': 0, 'form': None, 'id': 19, 'loss': 0,         'name': 'West Ham United FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'WHU', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1100, 'strength_overall_away': 1160, 'strength_attack_home': 1090, 'strength_attack_away': 1100, 'strength_defence_home': 1080, 'strength_defence_away': 1200},

# {'code': 39, 'draw': 0, 'form': None, 'id': 20, 'loss': 0,          'name': 'Wolverhampton Wanderers FC', 'played': 0, 'points': 0, 'position': 0, 'short_name': 'WOL', 'strength': 3, 'team_division': None, 'unavailable': False, 'win': 0, 'strength_overall_home': 1110, 'strength_overall_away': 1200, 'strength_attack_home': 1180, 'strength_attack_away': 1200, 'strength_defence_home': 1080, 'strength_defence_away': 1150}]
