import os

links = {
    'assunto-01': {
        'aula-01': 'link-para-aula.m3u8',
    },
    'assunto-02': {}
}


for day_k, day_v in links.items():
    print(f"Criando diretório {day_v}")
    os.system(f"mkdir '{day_k}'")
    for file_name, file_url in day_v.items():
        print(f"Convertendo o arquivo {file_name}")
        os.system(f"ffmpeg -v quiet -stats -i {file_url} -c copy -bsf:a aac_adtstoasc '{day_k}/{file_name}.mp4'")