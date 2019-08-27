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

s = m.stream.Score()
rh = m.stream.Part()
lh = m.stream.Part()
#help(rh)

# Violins
violin1 = parts[0]
violin2 = parts[1]
print ("stream.Part violin1: wellformed " + str(violin1.isWellFormedNotation()) + " type: "+str(type(violin1)))
violin3 = parts[2]
# Violas
viola1 = parts[3]
viola2 = parts[4]
viola3 = parts[5]

# The Violoncelli
violoncello1 = parts[6]
violoncello2 = parts[7]
violoncello3 = parts[8]

# The Contrabass
contrabass1 = parts[9]


# Create right hand
rh.insert(0,violin1)
print("rh.insert: wellformed "+str(rh.isWellFormedNotation()))
# Why is the stream rh notWellFormed after the insert ?
rh.append([violin2,violin3, viola1, viola2, viola3])
print("rh.append:  wellformed "+str(rh.isWellFormedNotation()))
print ("Why not wellformed?")
#rh.append(violin3)

#rh.append(viola1)
#rh.append(viola2)
#rh.append(viola3)


# Create left hand
lh.insert(0,violoncello1)
lh.append(violoncello2)
lh.append(violoncello3)

lh.append(contrabass1)
#lh.show()
# It works until here

s.insert(0,rh)
s.insert(0,lh)

# See: http://web.mit.edu/music21/doc/moduleReference/moduleLayout.html#staffgroup
staffGroup1 = m.layout.StaffGroup([rh, lh], name='Piano', abbreviation='Pno.', symbol='brace')
s.insert(0, staffGroup1)
#s.show()