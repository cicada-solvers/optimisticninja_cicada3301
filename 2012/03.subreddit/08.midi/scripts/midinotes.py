import mido

def getNotes(filename, track):
    result = ''
    for msg in mido.MidiFile(filename).tracks[track]:
        if msg.type == 'note_off':
            result += f'{msg.note} {msg.time}\r\n'
    return result

def notesToSingleLetters(msg):
    result = ''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    dict = {}
    for line in msg.splitlines():
        if line in dict:
            result += dict[line]
        else:
            letter = letters.pop(0)
            result += letter
            dict[line] = letter
    return result

print(notesToSingleLetters(getNotes('cicada-3301-2012-midi-song.midi', 1)))
