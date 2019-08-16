# Filenaam: test_music21_py3.py
# Functie: test music21 library na install
# Opmerking: uitgangspunt lilypond en musescore3 zijn geinstalleerd

# from music21 import * 
import music21 as m


# Zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/usr/bin/musescore3'

# Debug environment
#for key in sorted(env.keys()):
#    print(key)
# print("getSettingsPath: "+str(env.getSettingsPath()))

# Toon een predefined score
s = m.corpus.parse('bach/bwv65.2.xml')
s.show()
 
# littleMelody = m.converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
# littleMelody.show()
# Onderstaande command vereist de environment setting midiPath
# littleMelody.show('midi')
