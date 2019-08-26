# Filenaam: convert_str_orch_to_piano_musescore_bvw1048_music21_py3.py
# Functie : Voorbeeld mbt bladmuziek in MuseScore formaat met losse stemmen
#           obv (BWV1048 3e Brandeburger Concert 1e deel)
#           omvormen tot bladmuziek voor piano
#
# 

import music21 as m

padBladmuziek = "~/Documents/sources/python/python3/python3_music21"
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

curr_stream = m.converter.parse(padBladmuziek+'/'+museScoreFile, format='musicxml')
# curr_stream.show()
parts = curr_stream.getElementsByClass(m.stream.Part)

aantalStemmen = len(parts)
print ("aantalStemmen: ", str(aantalStemmen))
#left_hand = parts[0]
#right_hand = parts[1]

# De violen
viool1 = parts[0]
viool2 = parts[1]
viool3 = parts[2]

# De altviolen
altviool1 = parts[3]
altviool2 = parts[4]
altviool3 = parts[5]

# De Celli
cello1 = parts[6]
cello2 = parts[7]
cello3 = parts[8]

# De Contrabas
contrabas1 = parts[9]
#print(contrabas1.partName)
#contrabas1.show()

# Plaats Viool I t/m III en altviolen I t/m III op balk voor de g-sleutel tbv rechter hand
rh = m.stream.Stream()
rh.append(viool1)
rh.append(viool2)
rh.append(viool3)

rh.append(altviool1)
rh.append(altviool2)
rh.append(altviool3)
#rh.show()
# Tot hier werkt het

# probleem: chordify zorgt voor malformed part object.
rh_akkoorden = rh.chordify()
# rh_akkoorden.show()

# Plaats Violoncello I t/m III + Contrabas op balk voor de f-sleutel tbv linker hand

