# Filenaam: chordify_musescore_bvw1048_music21_py3.py
# Functie : Voorbeeld mbt bladmuziek in MuseScore formaat met losse stemmen
#           omvormen tot accoorden
#
# 

import music21 as m

padBladmuziek = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV1048_Brandenburg_Concerto_No_3_in_G_Major_in_parts_orgineel.musicxml"

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
bladmuziekMetAccoorden.show()

