# Filenaam: read_musescore_file_music21_py3.py
# Functie : Voorbeeld mbt inlezen van bladmuziek in MuseScore formaat
# 

import music21 as m

padBladmuziek = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV_974_Adagio_Marcello_v000c.musicxml"

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
# Toon bladmuziek
#bladmuziek.show()

# Bepaal eigenschappen van de bladmuziek
aantalStemmen1 = len(bladmuziek.parts)
aantalStemmen2 = len(bladmuziek.getElementsByClass('Part'))
print("Aantal stemmen: "+str(aantalStemmen1) + " "+ str(aantalStemmen2))
aantalMatenPart0 = len(bladmuziek.parts[0].getElementsByClass('Measure'))
aantalMatenPart1 = len(bladmuziek.parts[1].getElementsByClass('Measure'))
print("Aantal maten stem0: "+str(aantalMatenPart0))
print("Aantal maten stem1: "+str(aantalMatenPart1))
partName0 = bladmuziek.parts[0].partName
print("Partname0: "+str(partName0))

# Mbv Help functie kan men informatie opvragen over objecten
# x = help(bladmuziek)
# x = help(bladmuziek.parts[0])
# print(x)
