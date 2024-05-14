# -*- coding: utf-8 -*-
"""kompres audio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-QJxmHq19kn0mKuYw2noU4Mz04iSVqdv
"""

!pip install pydub

from pydub import AudioSegment

def resize_audio(input_path, output_path, speed):
    # Load audio
    audio = AudioSegment.from_file(input_path)

    # Resize audio by changing playback speed
    resized_audio = audio.speedup(playback_speed=speed)

    # Export resized audio
    resized_audio.export(output_path, format="mp3")
    print(f"Audio resized and saved to {output_path}")

# Upload audio file
from google.colab import files
uploaded = files.upload()

# Specify input and output paths
input_path = next(iter(uploaded))
output_path = "hasilkompresaudio.mp3"  # Change the output path if needed

# Specify speed factor for resizing audio duration
speed_factor = 1.5  # Change the speed factor as needed (1.0 means no change)

# Resize audio
resize_audio(input_path, output_path, speed_factor)