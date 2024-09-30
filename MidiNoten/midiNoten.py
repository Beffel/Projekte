import mido
from mido import MidiFile, MidiTrack, Message

# Define a function to create a MIDI file
def create_midi(patterns, filename):
    mid = MidiFile()
    
    for pattern in patterns:
        track = MidiTrack()
        mid.tracks.append(track)
        
        for msg in pattern:
            track.append(msg)
    
    mid.save(filename)

# Kick drum pattern (4/4)
kick_pattern = [
    Message('note_on', note=36, velocity=100, time=0),
    Message('note_off', note=36, velocity=0, time=480)
] * 4

# Hi-Hats pattern (Closed on off-beats, occasional open)
hh_pattern = [
    Message('note_on', note=42, velocity=80, time=240),  # Closed hi-hat
    Message('note_off', note=42, velocity=0, time=480),
    Message('note_on', note=46, velocity=80, time=720),  # Open hi-hat
    Message('note_off', note=46, velocity=0, time=480)
] * 2

# Percussion pattern (syncopated claps and snares)
perc_pattern = [
    Message('note_on', note=39, velocity=90, time=960),  # Clap
    Message('note_off', note=39, velocity=0, time=480),
    Message('note_on', note=38, velocity=90, time=1440), # Snare
    Message('note_off', note=38, velocity=0, time=480)
] * 2

# Bassline pattern (simple, repetitive)
bass_pattern = [
    Message('note_on', note=36, velocity=100, time=0),
    Message('note_off', note=36, velocity=0, time=240),
    Message('note_on', note=38, velocity=100, time=480),
    Message('note_off', note=38, velocity=0, time=240),
    Message('note_on', note=41, velocity=100, time=480),
    Message('note_off', note=41, velocity=0, time=240),
    Message('note_on', note=43, velocity=100, time=480),
    Message('note_off', note=43, velocity=0, time=240)
]

# Arpeggio pattern (evolving)
arp_pattern = [
    Message('note_on', note=60, velocity=100, time=0),
    Message('note_off', note=60, velocity=0, time=240),
    Message('note_on', note=64, velocity=100, time=480),
    Message('note_off', note=64, velocity=0, time=240),
    Message('note_on', note=67, velocity=100, time=480),
    Message('note_off', note=67, velocity=0, time=240),
    Message('note_on', note=72, velocity=100, time=480),
    Message('note_off', note=72, velocity=0, time=240)
]

# Pad pattern (chords)
pad_pattern = [
    Message('note_on', note=48, velocity=80, time=0),
    Message('note_on', note=52, velocity=80, time=0),
    Message('note_on', note=55, velocity=80, time=0),
    Message('note_off', note=48, velocity=0, time=1920),
    Message('note_off', note=52, velocity=0, time=0),
    Message('note_off', note=55, velocity=0, time=0),
    Message('note_on', note=50, velocity=80, time=0),
    Message('note_on', note=53, velocity=80, time=0),
    Message('note_on', note=57, velocity=80, time=0),
    Message('note_off', note=50, velocity=0, time=1920),
    Message('note_off', note=53, velocity=0, time=0),
    Message('note_off', note=57, velocity=0, time=0)
]

# Create the MIDI file
patterns = [kick_pattern, hh_pattern, perc_pattern, bass_pattern, arp_pattern, pad_pattern]

create_midi(patterns, 'C:\Users\Student\VSC_Studio_Code\Python\Sortieren\Projekte\MidiNoten\techno2_track_patterns.mid')

'/mnt/data/techno_track_patterns.mid'

