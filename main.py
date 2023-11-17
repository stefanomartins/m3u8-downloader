import ffmpeg
import os
import concurrent.futures

links = {"subject-01": {}, "subject-02": {}}


def download_file(file_name: str, file_url: str):
    ffmpeg.input(
        file_url,
    ).output(
        f"{file_name}.mp4", absf="aac_adtstoasc", c="copy"
    ).run(quiet=True, overwrite_output=True)


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = []
        for day_k, day_v in links.items():
            if not os.path.exists(day_k):
                print(f"Criando diretório {day_k}")
                os.mkdir(day_k)

            for file_name, file_url in day_v.items():
                print(f"Convertendo o arquivo {file_name}")

                results.append(
                    executor.submit(download_file, f"{day_k}/{file_name}", file_url)
                )

                # NOTE: Old syntax. Commented for historic purposes.
                # os.system(f"ffmpeg -v quiet -stats -i {file_url} -c copy -bsf:a aac_adtstoasc '{day_k}/{file_name}.mp4'")


if __name__ == "__main__":
    main()
