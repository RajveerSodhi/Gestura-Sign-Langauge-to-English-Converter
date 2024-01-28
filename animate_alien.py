from moviepy.editor import *

def animate_alien(text):
    morse = encrypt(text)

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

    # loading video dsa gfg intro video
    clip = VideoFileClip("alien_morse.mp4")

    clip = clip.subclip(0)

    # previewing the clip at fps = 20
    clip.preview(fps=20)

animate_alien("--. --... .  ")