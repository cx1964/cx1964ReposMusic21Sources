# Filenaam: convert_str_orch_to_piano_musescore_bvw1048_music21_py3.py
# Functie : Sample of how to convert sheetmusic in MuseScore format with seperate voices
#           using BWV1048 3rd Brandeburger Concert 1st movement,
#           to sheetmusic for piano
#
# 

import music21 as m

scorePath = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV1048_Brandenburg_Concerto_No_3_in_G_Major_in_parts_orgineel_1st_mov.musicxml"


# Zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/usr/bin/musescore3'

curr_stream = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')
# curr_stream.show()
parts = curr_stream.getElementsByClass(m.stream.Part)

voiceCount = len(parts)
print ("voiceCount: ", str(voiceCount))

# Violins
violin1 = parts[0]
violin2 = parts[1]
violin3 = parts[2]

# Violas
alto = m.clef.AltoClef()
treble = m.clef.TrebleClef()
viola1 = parts[3]
viola2 = parts[4]
viola3 = parts[5]
# viola1.show('text')
# viola1.show()

# The Violoncelli
violoncello1 = parts[6]
violoncello2 = parts[7]
violoncello3 = parts[8]

# The Contrabass
contrabass1 = parts[9]
#print(contrabas1.partName)
#contrabas1.show()

# Create right hand
rh = m.stream.Stream()
rh.append(violin1)
rh.append(violin2)
rh.append(violin3)

rh.append(viola1)
rh.append(viola2)
rh.append(viola3)
# Check of Stream is well formed
# print(rh.isWellFormedNotation())
# rh is well formed
# rh.show('text')
#rh.show()

# Create left hand
lh = m.stream.Stream()
lh.append(violoncello1)
lh.append(violoncello2)
lh.append(violoncello3)

lh.append(contrabass1)
#lh.show()
# It works until here
