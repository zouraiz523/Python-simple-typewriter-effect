import sys
import time
import pygame

# Initialize the mixer module for audio playback
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load("music.mp3")  # Replace with your audio file name
pygame.mixer.music.play()  # Start playing the audio

# Lyrics list
lines = [
    "So I'ma love you every night like it's the last night",
    "Like it's the last night",
    "If the world was ending",
    "I'd wanna be next to you",
    "If the party was over",
    "And our time on Earth was through",
    "I'd wanna hold you just for a while",
    "And die with a smile",
    "If the world was ending",
    "I'd wanna be next to you",
    "Right next to you"
]

# Delays for each line
delays = [0.6, 0.7, 1.0, 0.4, 1.6, 1.3, 3.6, 1.7, 2.0, 0.9, 1.1]

def print_lyrics():
    for line, delay in zip(lines, delays):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.1)  # Typing effect for each character
        print()  # New line after each line
        time.sleep(delay)  # Delay between lines

# Run the lyrics function
print_lyrics()

# Stop the music after the lyrics are done
pygame.mixer.music.stop()
