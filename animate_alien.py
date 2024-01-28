from moviepy.editor import *
import sys


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
    return cipher

def animate_alien(text):
    morse = encrypt(text.upper())

    clip = [
        "default to thumb out",
        "default to fingers out",
        "fingers out to default",
        "fingers out to thumb out",
        "thumb out to default",
        "thumb out to fingers out",
        "fingers out to fingers out",
        "thumb out to thumb out"
    ]

    morse = morse.strip()
    result = []

    result.append("default to fingers out" if morse[0] == "." else "default to thumb out")
    for i in range(1, len(morse) - 1):
        if morse[i - 1] == "-" and morse[i] == "-":
            result.append("thumb out to thumb out")
        elif morse[i - 1] == "-" and morse[i] == ".":
            result.append("thumb out to fingers out")
        elif morse[i - 1] == "-" and morse[i] == " ":
            result.append("thumb out to default")
        elif morse[i - 1] == "." and morse[i] == "-":
            result.append("fingers out to thumb out")
        elif morse[i - 1] == "." and morse[i] == ".":
            result.append("fingers out to fingers out")
        elif morse[i - 1] == "." and morse[i] == " ":
            result.append("fingers out to default")
        elif morse[i - 1] == " " and morse[i] == "-":
            result.append("default to thumb out")
        elif morse[i - 1] == " " and morse[i] == ".":
            result.append("default to fingers out")

    final_videos = []
    for clip in result:
        final_videos.append(VideoFileClip("alien animation/" + clip + ".mp4"))

    final_video = concatenate_videoclips(final_videos, method="compose")
    final_video.write_videofile("alien_morse.mp4", verbose=False, logger=None, threads=64, fps=20)


animate_alien(sys.argv[1])