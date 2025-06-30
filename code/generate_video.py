### Milo Tek - 30/06/2025 - SFX Showcaser ###
## Create videos to showcase sound effects like this: TODO: ADD EXAMPLE HERE LOLOLOL

import os, sys, glob, json, moviepy as mp, numpy as np

### CONSTANTS ###
f = open("settings/config.json")
cfg = json.load(f)

folder = cfg["audio"]["folder"]
font = os.path.join("settings", "font.otf")
size = cfg["video"]["text_size"]
color = cfg["video"]["text_color"]


def create_clip(audio_path):
    try:
        audio_clip = mp.AudioFileClip(audio_path)
        text_clip = mp.TextClip(text=str(audio_path), font=font, font_size=size, color=color)
        video_clip = text_clip.with_audio(audio_clip)
        video_clip.duration = audio_clip.duration
        video_clip.fps = 16
        return video_clip
    except:
        print("error")



def get_sound_files(start_path="."):
    sounds = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            sounds.append(os.path.join(root, file))
            print(os.path.join(root, file))
    return sounds

sounds = get_sound_files(folder)
#clips = []

for x in range(0, len(sounds)):
    create_clip(sounds[x]).write_videofile(f"output/{x}.mp4")

#final = mp.concatenate_videoclips(clips)
#final.write_videofile("./result.mp4")