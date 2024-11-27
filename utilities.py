from pathlib import Path
from time import sleep

def get_file_by_partial_name(
    diretory_to_look_inside: Path,
    partial_name: str,
    seconds_to_wait_file: int = 1,
    case_sentive: bool = False,
) -> Path:
    if partial_name == "*":
        partial_name = ""

    if not case_sentive:
        partial_name = partial_name.upper()

    while seconds_to_wait_file:
        sleep(1)
        seconds_to_wait_file -= 1
        for content in diretory_to_look_inside.iterdir():
            content_name = content.name if case_sentive else content.name.upper()
            if content.is_file() and partial_name in content_name:
                return content

    raise Exception(
        f"Arquivo {partial_name} não encontrado em {diretory_to_look_inside}"
    )

def get_all_files_by_partial_name(
    diretory_to_look_inside: Path,
    partial_name: str,
    seconds_to_wait_file: int = 1,
    case_sentive: bool = False,
) -> Path:
    if partial_name == "*":
        partial_name = ""

    if not case_sentive:
        partial_name = partial_name.upper()

    files_list = []

    while seconds_to_wait_file:
        sleep(1)
        seconds_to_wait_file -= 1

        for content in diretory_to_look_inside.iterdir():
            content_name = content.name if case_sentive else content.name.upper()
            if content.is_file() and partial_name in content_name:
                files_list.append(content)
        return files_list

    raise Exception(
        f"Arquivo {partial_name} não encontrado em {diretory_to_look_inside}"
    )

def clean_directory(directory: Path, extensions_to_keep_files: list[str] = []):
    try:
        files = [item for item in directory.iterdir() if item.is_file()]
        dirs = [item for item in directory.iterdir() if item.is_dir()]
    except FileNotFoundError as e:
        raise
    for f in files:
        if all(
            [
                not f.name.upper().endswith(extension.upper())
                for extension in extensions_to_keep_files
            ]
        ):
            f.unlink()
    for d in dirs:
        clean_directory(d, extensions_to_keep_files)
        try:
            d.rmdir()
        except OSError:
            pass