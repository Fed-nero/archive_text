from algorithms import divide_list, generate_card_of_prefixes, generate_alphabet_card, convert
from stoto_mujiki import define_frequency_of_symbols
from subprocess import run, PIPE
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Архивация текста: input и опциональное имя выхода")
parser.add_argument("input_path", help="путь к файлу, откуда брать текст для архивации")
parser.add_argument("output_name", nargs="?", help="базовое имя для сохранения (без суффиксов)")
args = parser.parse_args()


P = args.input_path
base_dir = Path(P).parent

# card/rar — всегда одинаковые имена
RAR_PATH = base_dir / "archive_rar.txt"
CARD_PATH = base_dir / "archive_card.txt"

# имя для разархивированного — по опциональному output_name (или имени входного)
base = Path(args.output_name).stem if args.output_name else Path(P).stem
UNARHIVED_PATH = base_dir / f"{base}_unarhived.txt"
SEP_FOR_CARD_TEXT = ' -> '

def archive():
    alphabet, amount_of_symbols = define_frequency_of_symbols(P)


    frequency_card_mujiki = list(alphabet.values())
    prefix_map = generate_card_of_prefixes(frequency_card_mujiki)
    #print(prefix_map)

    a_c = generate_alphabet_card(prefix_map, alphabet)

    compresed_message = convert(P, a_c)

    compresed_blocks = []

    for i in range(0, len(compresed_message), 16):
        compresed_blocks.append(compresed_message[i:(i+16) if i+16<len(compresed_message) else len(compresed_message)])

    codes = [int(b, 2) for b in compresed_blocks]
    chars = [chr(c) for c in codes]



    with open(RAR_PATH, 'wt', encoding='utf-8') as file:
        file.write(''.join(chars))


    card_text = f'{amount_of_symbols}\n'
    

    for key, value in a_c.items():
        card_text+=f'{value}{SEP_FOR_CARD_TEXT}{key}'
        if not key=='\n':
            card_text+='\n'


    with open(CARD_PATH, 'wt', encoding='utf-8') as file:
        file.write(card_text)



def unarchive():
    with open(RAR_PATH, 'rt', encoding='utf-8') as file:
        chars = list(file.read())

    code_b = [ord(c) for c in chars]
    binary_blocks = [f'{code:016b}' for code in code_b]
    str_binary = ''.join(binary_blocks)
    card = {}
    with open(CARD_PATH, 'rt', encoding='utf-8') as file:
        amount_of_s = int(file.readline())
        for line in file.readlines():
            data = line.rstrip('\n').split(SEP_FOR_CARD_TEXT)
            value = data[0]
            key = '\n' if data[1] == '' else data[1]
            card[value] = key
    return card, str_binary, amount_of_s

    

archive()

c, str_binary, norm_text_len = unarchive()

str_of_symbol = ''
unarchived_text = ''

print(f'{c=}')
print(f'{str_binary=}')

print(norm_text_len)

for i in str_binary:
    str_of_symbol+=i
    if str_of_symbol in c:
        print(str_of_symbol)
        unarchived_text+=c[str_of_symbol]
        str_binary = str_binary[len(str_of_symbol):len(str_binary)]
        str_of_symbol = ''

with open(UNARHIVED_PATH, 'wt', encoding='utf-8') as file:
    file.write(unarchived_text)