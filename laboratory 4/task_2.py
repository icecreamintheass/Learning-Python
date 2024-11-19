# TODO импортировать необходимые модули
import csv
import json
import io  # Корректная типизация

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        assert isinstance(json_file, io.TextIOWrapper)
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    # TODO проверить содержимое выходного файла
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")