def find_common_participants(group1, group2, delimiter=","):
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    common_list = sorted(participants1 & participants2)  # Находим пересечение и сортируем

    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result_common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", result_common_participants)
