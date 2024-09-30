# Techno Track Patterns - MIDI File Generator

This project is a Python script that generates a techno track by composing various MIDI patterns (Kick, Hi-Hats, Percussion, Bassline, Arpeggio, and Pad). The generated patterns are combined into a single MIDI file.

## Project Structure

- **`create_midi(patterns, filename)`**: This is the core function that generates the MIDI file. It takes a list of MIDI patterns and a filename as input and creates a `.mid` file with separate tracks for each pattern.
  
## MIDI Patterns

The following patterns are defined in the script:

1. **Kick Drum Pattern** (`kick_pattern`):
   - A simple 4/4 kick drum sequence using MIDI note 36 (Bass Drum).
   - Repeated 4 times to complete a measure.

2. **Hi-Hats Pattern** (`hh_pattern`):
   - Alternates between closed hi-hats (MIDI note 42) on off-beats and open hi-hats (MIDI note 46) occasionally.

3. **Percussion Pattern** (`perc_pattern`):
   - A syncopated pattern with claps (MIDI note 39) and snares (MIDI note 38).

4. **Bassline Pattern** (`bass_pattern`):
   - A repetitive, simple bassline cycling through notes 36, 38, 41, and 43.

5. **Arpeggio Pattern** (`arp_pattern`):
   - A melodic sequence that ascends through notes 60 (C), 64 (E), 67 (G), and 72 (C an octave higher).

6. **Pad Pattern** (`pad_pattern`):
   - Chord sequences with sustained notes. The first chord uses notes 48, 52, and 55. The second chord follows with notes 50, 53, and 57.

## How to Run the Script

1. Ensure that Python and the `mido` library are installed. You can install `mido` via pip:

   ```bash
   pip install mido
