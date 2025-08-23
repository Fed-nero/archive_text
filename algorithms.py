from copy import deepcopy  # Импортируем функцию deepcopy для глубокого копирования объектов


def generate_card_of_prefixes(l):
    # Функция генерирует словарь префиксов, соответствующих разделению списка l
    initial_map = {'': l}  # Начальный словарь: ключ — пустая строка, значение — исходный список
    # Повторяем, пока не все значения в словаре станут числами (int или float)
    while not all(map(lambda d: isinstance(d, (int, float)), initial_map.values())):
        initial_map_two = deepcopy(initial_map)  # Создаём копию, чтобы безопасно модифицировать словарь
        # Проходим по всем текущим записям словаря
        for key, value in initial_map.items():
            # Пропускаем, если значение уже число или пустой список
            if isinstance(value, (int, float)) or (isinstance(value, list) and len(value) == 0):
                continue
            # Разделяем список value на две части: одну под новую «0»-ветку, другую под «1»-ветку
            result = divide_list([value, []])
            l_one, l_two = result  # Распаковываем результат: l_one и l_two
            # Если оба списка пустые (не удалось разделить), завершаем работу
            if not l_one and not l_two:
                exit(0)
            # Удаляем старую запись и добавляем две новые с префиксами '0' и '1'
            del initial_map_two[key]
            initial_map_two[key + '0'] = l_one
            initial_map_two[key + '1'] = l_two
        # Обновляем рабочий словарь
        initial_map = deepcopy(initial_map_two)
    return initial_map  # Возвращаем итоговую карту префиксов и числовых значений


def divide_list(ll):
    # Функция разделяет список ll на две части с минимальной разницей сумм

    def find_closest_number(num, l):
        # Находит в списке l число, которое максимально приближено к num, но меньше его
        list_of_differences = [n - num for n in l if n <= num]  # Разности меньше нуля
        best_index = 0

        # Если нет подходящих чисел, возвращаем None
        if not len(list_of_differences):
            return None
        # Ищем наибольшую разность (то есть число, ближе всего к num)
        for idx, value in enumerate(list_of_differences):
            if value > list_of_differences[best_index]:
                best_index = idx
        # Преобразуем разность обратно в исходное число
        return int(list_of_differences[best_index] + num)

    def hard_task_mujiki(l_main: list):
        # Основная логика: перебалансировка элементов между двумя частями
        l_two, l_one = l_main[0], l_main[1]  # Первая и вторая часть
        # Если обе части — списки, пытаемся перенести элемент
        if isinstance(l_one, list) and isinstance(l_two, list):
            difference = abs(sum(l_one) - sum(l_two))  # Текущая разница сумм
            needed_num = difference / 2  # Число, которое нужно найти и перенести
            closest_num = find_closest_number(needed_num, l_two)  # Ищем подходящий элемент в l_two

            # Если нашли число и оно меньше needed_num, переносим его
            if closest_num is not None and closest_num <= needed_num:
                l_two.remove(closest_num)
                l_one.append(closest_num)
            # Если в какой-то части остался один элемент, преобразуем список в число
            if len(l_two) == 1:
                l_two = l_two[0]
            if len(l_one) == 1:
                l_one = l_one[0]
        return [l_two, l_one]  # Возвращаем новые части

    # Первый вызов перераспределения
    r = hard_task_mujiki(ll)
    r_previous = None
    # Повторяем, пока результат перестанет изменяться
    while r != r_previous:
        r_previous = deepcopy(r)
        r = hard_task_mujiki(r)

    return r  # Итоговое разделение списка


def generate_alphabet_card(p_m, a):
    a_p = {}

    for key_a, value_a in a.items():
        for key_p_m, value_p_m in p_m.items():
            if value_a == value_p_m:
                a_p[key_a] = key_p_m
                del p_m[key_p_m]
                break
    return a_p


def convert(path, card):
    str_converted = ''
    with open(path, 'rt', encoding='utf-8') as file:
        for row in file:
            for symbol in row:
                str_converted+=card[symbol]
    return str_converted
