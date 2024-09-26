from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    x = 0
    for item in strings:
        x += 1
        y = file.tell()
        position = (x, y)
        file.write(item + '\n')
        strings_positions[position] = item
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
