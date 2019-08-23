# Filenaam: chordify_musescore_bvw1048_music21_py3.py
# Functie : Voorbeeld mbt bladmuziek in MuseScore formaat met losse stemmen
#           omvormen tot accoorden
#
# 

import music21 as m

padBladmuziek = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV1048_Brandenburg_Concerto_No_3_in_G_Major_in_parts_orgineel_1st_mov.musicxml"
keyG = m.key.Key('G') # BWV1048 1 st move is in G major

# Zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/usr/bin/musescore3'

bladmuziek = m.converter.parse(padBladmuziek+'/'+museScoreFile, format='musicxml')
bladmuziekMetAccoorden = bladmuziek.chordify()
# Toon bladmuziek
#bladmuziekMetAccoorden.show()

# help(bladmuziekMetAccoorden)

# Harmonische Analyse (benoem akkoorden)
for akkoord in bladmuziekMetAccoorden.recurse().getElementsByClass('Chord'):
    # print ("Akkoord: " + str(chord))
    rn = m.roman.romanNumeralFromChord(akkoord, keyG)
    # print ("rn= " + str(rn))
    # benoem akkoord obv romeinse cijfers
    akkoord.addLyric(str(rn.figure))
bladmuziekMetAccoorden.show()    