import os

links = {}

for k,v in links.items():
    print(f"Convertendo arquivo {k}")
    os.system(f"ffmpeg -i {v} -c copy -bsf:a aac_adtstoasc {k}.mp4")