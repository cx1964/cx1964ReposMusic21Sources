# Filenaam: convert_str_orch_to_piano_musescore_bvw1048_music21_py3.py
# Functie : Sample of how to convert sheetmusic in MuseScore format with seperate voices
#           using BWV1048 3rd Brandeburger Concert 1st movement,
#           to sheetmusic for piano
#


import music21 as m

scorePath = "~/Documents/sources/python/python3/python3_music21"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "BWV1048_Brandenburg_Concerto_No_3_in_G_Major_in_parts_orgineel_1st_mov.musicxml"

outputFormat = 'musicxml'
outputFile = scorePath+'/output.'+outputFormat

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

s = m.stream.Score()
rh = m.stream.Part() 
lh = m.stream.Part()
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
measureCountViola1 = len (m.stream.iterator.RecursiveIterator(viola1, streamsOnly=True))
print("Aantal measures viola1: "+ str(measureCountViola1))
# check all clefs
#for i in list(range(measureCountViola1)):
#    print("cleff("+str(i+1)+"): "+str(viola3.measure(i+1).clef) )
measureCountViola2 = len (m.stream.iterator.RecursiveIterator(viola2, streamsOnly=True))
print("Aantal measures viola2: "+ str(measureCountViola2))
measureCountViola3 = len (m.stream.iterator.RecursiveIterator(viola3, streamsOnly=True))
print("Aantal measures viola3: "+ str(measureCountViola3))


# The Violoncelli
violoncello1 = parts[6]
violoncello2 = parts[7]
violoncello3 = parts[8]

# The Contrabass
contrabass1 = parts[9]

measureCountContrabass1 = len (m.stream.iterator.RecursiveIterator(contrabass1, streamsOnly=True))
print("Aantal measures contrabass1: "+ str(measureCountContrabass1))

# Change octava8 Bassclefs of contrabass into bassClef
contrabass1.measure(1).clef = m.clef.BassClef()

# Create right hand
rh.append(violin1)
rh.append(violin2)
rh.append(violin3)
rh.append(viola1)
rh.append(viola2)
rh.append(viola3)
#rh.show()
#rh.write(outputFormat, outputFile)

# Create left hand
lh.append([violoncello1, violoncello2, violoncello3, contrabass1])
#lh.show()


s.insert(0,rh)
s.insert(0,lh)

# See: http://web.mit.edu/music21/doc/moduleReference/moduleLayout.html#staffgroup
staffGroup1 = m.layout.StaffGroup([rh, lh], name='Piano', abbreviation='Pno.', symbol='brace')
s.insert(0, staffGroup1)
#s.write(outputFormat, outputFile)
#s.show()

print("Clefs of violas and contrabass are properly set to the wanted type.")
print("How can you append all parts of RH and all parts of LH?")

# The problem
#print("There is no problem if you use one append for the right and one append for the right hand.")
#print("When you insert and append or append two times in the left and/or right hand the stream get corrupted.")
#print("Why?")

'''
Error message:

Measure 546, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 547, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 548, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 549, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 550, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 551, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 552, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 553, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 554, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 555, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 556, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 557, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 558, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 559, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 560, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 561, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 562, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 563, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 564, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 565, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 566, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 567, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 568, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 569, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 570, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 571, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 572, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 573, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 574, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 575, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 576, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 577, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 578, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 579, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 580, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 581, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 582, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 583, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 584, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 585, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 586, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 587, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 588, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 589, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 590, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 591, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 592, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 593, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 594, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 595, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 596, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 597, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 598, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 599, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 600, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 601, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 602, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 603, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 604, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 605, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 606, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 607, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 608, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 609, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 610, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 611, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 612, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 613, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 614, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 615, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 616, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 617, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 618, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 619, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 620, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 621, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 622, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 623, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 624, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 625, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 626, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 627, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 628, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 629, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 630, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 631, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 632, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 633, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 634, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 635, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 636, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 637, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 638, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 639, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 640, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 641, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 642, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 643, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 644, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 645, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 646, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 647, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 648, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 649, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 650, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 651, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 652, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 653, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 654, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 655, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 656, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 657, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 658, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 659, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 660, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 661, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 662, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 663, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 664, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 665, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 666, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 667, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 668, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 669, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 670, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 671, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 672, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 673, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 674, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 675, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 676, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 677, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 678, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 679, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 680, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 681, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 682, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 683, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 684, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 685, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 686, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 687, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 688, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 689, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 690, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 691, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 692, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 693, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 694, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 695, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 696, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 697, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 698, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 699, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 700, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 701, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 702, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 703, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 704, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 705, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 706, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 707, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 708, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 709, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 710, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 711, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 712, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 713, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 714, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 715, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 716, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 717, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 718, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 719, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 720, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 721, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 722, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 723, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 724, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 725, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 726, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 727, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 728, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 729, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 730, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 731, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 732, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 733, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 734, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 735, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 736, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 737, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 738, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 739, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 740, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 741, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 742, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 743, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 744, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 745, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 746, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 747, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 748, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 749, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 750, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 751, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 752, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 753, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 754, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 755, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 756, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 757, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 758, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 759, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 760, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 761, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 762, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 763, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 764, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 765, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 766, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 767, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 768, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 769, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 770, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 771, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 772, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 773, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 774, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 775, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 776, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 777, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 778, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 779, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 780, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 781, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 782, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 783, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 784, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 785, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 786, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 787, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 788, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 789, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 790, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 791, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 792, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 793, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 794, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 795, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 796, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 797, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 798, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 799, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 800, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 801, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 802, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 803, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 804, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 805, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 806, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 807, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 808, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 809, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 810, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 811, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 812, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 813, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 814, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 815, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 816, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 817, staff 2 incomplete. Expected: 4/4; Found: 0/1
Measure 818, staff 2 incomplete. Expected: 2/4; Found: 0/1

'''