# Filename: convert_str_orch_to_piano_musescore_bvw1048_music21_py3.py
# Function: Sample of how to convert sheetmusic in MuseScore format with seperate voices
#           using BWV1048 3rd Brandeburger Concert 1st movement,
#           to sheetmusic for piano
# Comment: For Music21 documentation see: https://web.mit.edu/music21/doc/index.html
#          For samples see https://github.com/cuthbertLab/music21-tools

import music21 as m

scorePath = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV1048_Brandenburg_Concerto_No_3_in_G_Major_in_parts_orgineel_1st_mov.musicxml"

# Set Meta Data
composer = 'J.S. Bach (1685 - 1750'
title = museScoreFile

outputFormat = 'musicxml'
outputFileDFLT = scorePath+'/output.'+outputFormat

# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
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

# change clefs of violas
#curr_stream.getElementsByClass(m.stream.Part)[3].measure(1).clef = m.clef.TrebleClef()
#curr_stream.getElementsByClass(m.stream.Part)[4].measure(1).clef = m.clef.TrebleClef()
#curr_stream.getElementsByClass(m.stream.Part)[5].measure(1).clef = m.clef.TrebleClef()
# change clefs of contrabas
#curr_stream.getElementsByClass(m.stream.Part)[9].measure(1).clef = m.clef.BassClef()
#curr_stream.show()


s = m.stream.Score()
rh = m.stream.Score() # .Part() only nest, Score can be used to chordify rh
lh = m.stream.Score() # .Part() only nest, Score can be used to chordify lh
#help(rh)

# Violins
violin1 = parts[0]
violin2 = parts[1]
violin3 = parts[2]

# Violas
viola1 = parts[3]
viola2 = parts[4]
viola3 = parts[5]

# parts[x].measure(1) contains info about measure1 of part[x]
# parts[3].measure(1).timeSignature
# parts[3].measure(1).clef

# Change Alto clefs of violas into TrebleClef
#print ("before parts[3].measure(1).clef: "+ str(parts[3].measure(1).clef))
#parts[3].write(outputFormat, scorePath+"/alto."+outputFormat)
viola1.measure(1).clef = m.clef.TrebleClef()
viola2.measure(1).clef = m.clef.TrebleClef()
viola3.measure(1).clef = m.clef.TrebleClef()
# parts[3].write(outputFormat, scorePath+"/treble."+outputFormat)

# check number of measures viola1 util 3
#measureCountViola1 = len (m.stream.iterator.RecursiveIterator(viola1, streamsOnly=True))
#print("Number of measures viola1: "+ str(measureCountViola1))
# check all clefs
#for i in list(range(measureCountViola1)):
#    print("cleff("+str(i+1)+"): "+str(viola3.measure(i+1).clef) )
#measureCountViola2 = len (m.stream.iterator.RecursiveIterator(viola2, streamsOnly=True))
#print("Number of measures viola2: "+ str(measureCountViola2))
#measureCountViola3 = len (m.stream.iterator.RecursiveIterator(viola3, streamsOnly=True))
#print("Number of measures viola3: "+ str(measureCountViola3))


# The Violoncelli
violoncello1 = parts[6]
violoncello2 = parts[7]
violoncello3 = parts[8]

# The Contrabass
contrabass1 = parts[9]

#measureCountContrabass1 = len (m.stream.iterator.RecursiveIterator(contrabass1, streamsOnly=True))
#print("Number of measures contrabass1: "+ str(measureCountContrabass1))

# Change octava8 Bassclefs of contrabass into bassClef
contrabass1.measure(1).clef = m.clef.BassClef()

# Create right hand
rh.append(violin1)
rh.append(violin2)
rh.append(violin3)
rh.append(viola1)
rh.append(viola2)
rh.append(viola3)
rh=rh.chordify()
# reset PartName
rh.partName = ""
rh.partAbbreviation = ""
# Why is this not set?
rh.instrumentName = "Piano"
rh.midiProgram="Piano"

# Inputfile measure 12 and 13 ares differtent for violin1, violin2 an violin3
#rh.show()
outputFile = scorePath + "/rh."+outputFormat
#rh.write(outputFormat, outputFile)

# Create left hand
lh.append(violoncello1)
lh.append(violoncello2)
lh.append(violoncello3)
lh.append(contrabass1)
lh=lh.chordify()
# reset PartName
lh.partName = ""
lh.partAbbreviation = ""
# Why is this not set?
lh.insert(m.instrument.Piano())

#lh.show()
outputFile = scorePath + "/lh."+outputFormat
#lh.write(outputFormat, outputFile)

s.insert(0,rh)
#print("type(s): "+str(type(s)))

s.insert(0,lh)
#print("type(s): "+str(type(s)))

# See: http://web.mit.edu/music21/doc/moduleReference/moduleLayout.html#staffgroup
staffGroup1 = m.layout.StaffGroup([rh, lh], name='Piano', abbreviation='Pno.', symbol='brace')
s.insert(0, staffGroup1)
outputFile = outputFileDFLT
s.write(outputFormat, outputFile)
s.insert(0, m.metadata.Metadata())
s.metadata.title = title
s.metadata.composer = composer
s.show()
#print("type(s): "+str(type(s)))
print("Program finished")

