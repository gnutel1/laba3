# TODO Напишите функцию find_common_participants
# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c=','):
    a1 = set(a.split(c))
    b1 = set(b.split(c))
    ab = sorted(a1.intersection(b1))
    return ab


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
d = find_common_participants(participants_first_group, participants_second_group, '|')
print(d)