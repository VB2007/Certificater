from os import getcwd
import eel

path = getcwd()

eel.init(path + "\\Web")

'''
Сделано:
Русские символы в названии файлов
Возможность не склонять ФИО
Модификация склонения (по отчеству, если его нет, то morphy)
НЕ СКЛОНЯТЬ другие текстовые поля
При наличии не используемых полей возникает ошибка

Надо сделать:
Не открывать и закрывать каждый раз Power Point
'''


@eel.expose
def start(input_file_name, output_file_name):
    from PPTX_to_PDF import main
    from all_names import all_names
    from PPTX_GENERATOR import PPTX_GENERATOR
    import os
    import shutil
    data = all_names(input_file_name, output_file_name)
    # То что ниже нужно для тестинга
    # data = all_names('data.xlsx', 'tmplt1.pptx')

    os.makedirs(f"GENERATED_PPTX/{data[0]['date']}",
                exist_ok=True)
    os.makedirs(f"GENERATED_PDF/{data[0]['date']}",
                exist_ok=True)

    shutil.rmtree(f"GENERATED_PPTX/{data[0]['date']}")
    shutil.rmtree(f"GENERATED_PDF/{data[0]['date']}")

    os.makedirs(f"GENERATED_PPTX/{data[0]['date']}",
                exist_ok=True)
    os.makedirs(f"GENERATED_PDF/{data[0]['date']}",
                exist_ok=True)
    for loc in data:
        file_name = PPTX_GENERATOR(loc)
        # command = "python PPTX_to_PDF.py " + file_name + " " + loc['date']
        main(file_name, loc['date'])
        # file = file_name.replace("©", " ")

if __name__ == "__main__":
    eel.start("HomePage.html", geometry={"size": (600, 400), "position": (400, 600)}, port=8002)
