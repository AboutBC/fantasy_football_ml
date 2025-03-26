players = [{
   'name': 'A.J. Brown',
   'catches': 88,
   'targets': 145,
   'yards': 1000
   },
   {
   'name': 'CeeDee Lamb',
   'catches': 107,
   'targets': 156,
   'yards': 1100
   },
   {
   'name': 'Justin Jefferson',
   'catches': 128,
   'targets': 184,
   'yards': 1500
   },
]

for player in players:
    name = player["name"]
    catches = player["catches"]
    targets = player["targets"]
    yards = player["yards"]
    catch_rate = catches/targets
    yards_per_catch = yards/catches
    yards_per_target = yards/targets
    print(name + ' has a catch rate of ' + str(catch_rate))
    print(name + str(yards_per_catch) + 'yards per catch')
    print(name + str(yards_per_target) + 'yards per target')