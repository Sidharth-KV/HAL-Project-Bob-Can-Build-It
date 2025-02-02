import edge_tts
import asyncio
import pygame
import os



async def text_to_speech(text, output_file, voice="en-US-JennyNeural", rate="+20%"):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(output_file)

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


input_file = r"C:\Users\Lenovo\Desktop\New folder\temp\temp.txt"
text  = "" 
if os.path.exists(input_file):
    with open(input_file, 'r') as file:
        file.read()
else:
    print("File does not exist")

output_file = r"C:\Users\Lenovo\Desktop\New folder\temp\temp.mp3"

asyncio.run(text_to_speech(text, output_file))
play_audio(output_file)
