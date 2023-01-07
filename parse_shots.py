# Given a CSV Shots file, calculates...
    # Speed of each player's shots separated by shot type

import csv

import sys
sys.dont_write_bytecode = True
sys.path.append('source')

from shot import Shot

# Input Arguments
if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<SwingVision Shots CSV File>'
    sys.exit()

# Parse input file into list of Shots
shots = []
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) # Skips Header Row

    for row in reader:
        player = row[0]
        shot_count = int(row[1])
        type = row[2]
        stroke = row[3]
        spin = row[4]
        speed = float(row[5]) # mph

        shot = Shot(player, shot_count, type, Shot.Stroke.string_to_enum(stroke), Shot.Spin.string_to_enum(spin), speed)
        shots.append(shot)

# Calculate Averages for each Spin Type for each Stroke Type
class Average:
    mCount = 0
    mRollingValue = 0.0

    def __init__(self):
        self.mCount = 0
        self.mRollingValue = 0.0

map = {} # Map<player-name, Map<Stroke Type, Map<Spin Type, Average> > >
for i in range(0, len(shots)):
    # Copies of Shot info
    player = shots[i].mPlayer
    stroke = shots[i].mStroke
    spin = shots[i].mSpin
    speed = shots[i].mSpeed

    # Add Map for player if not already existing
    if player not in map:
        map[player] = {}

    # Add Stroke in map if not already existing
    if stroke not in map[player]:
        map[player][stroke] = {}

    # Add Spin in map if not already existing
    if spin not in map[player][stroke]:
        map[player][stroke][spin] = Average()

    # Recalculate rolling average
    map[player][stroke][spin].mRollingValue = (map[player][stroke][spin].mRollingValue * map[player][stroke][spin].mCount + speed) / (map[player][stroke][spin].mCount + 1)
    map[player][stroke][spin].mCount = map[player][stroke][spin].mCount + 1

# Print Results
for player in map:
    print player
    for stroke in map[player]:
        print '\t', Shot.Stroke.enum_to_string(stroke)
        for spin in map[player][stroke]:
            print '\t\t', Shot.Spin.enum_to_string(spin), ':', round(map[player][stroke][spin].mRollingValue,2), 'mph (' + str(map[player][stroke][spin].mCount) + ')'
    print ''
