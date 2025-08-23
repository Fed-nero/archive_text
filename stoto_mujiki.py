def define_frequency_of_symbols(path):
    symbols = {}
    amount_of_symbols = 0
    with open(path, 'rt', encoding='utf-8') as file:
        for row in file:
            for symbol in row:
                symbols[symbol] =symbols.get(symbol, 0)+1
                amount_of_symbols+=1
    return symbols, amount_of_symbols
