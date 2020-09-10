# unit4 = ('',) + tuple('万億兆京垓秭穣溝澗正載極')
unit4 = ('',) + tuple('万億兆')
unit1 = ('',) + tuple('拾百千')
digits = tuple('零壱弍参四五六七八九')
arabic4 = {unit[:1]: 10000**i for i, unit in enumerate(unit4)}
arabic1 = {unit: 10**i for i, unit in enumerate(unit1)}
arabics = {digit: i for i, digit in enumerate(digits)}


def int_to_kanji(arabic):
    if not arabic.isdecimal():
        return 'error'
    if len(str(arabic)) > 16:
        return 'error'
    arabic = int(arabic)
    if arabic == 0:
        return digits[0]
    sign = '-' if arabic < 0 else ''
    arabic = abs(arabic)
    def convert():
        for column, digit in enumerate(map(int, str(arabic)[::-1])):
            if column % 4 == 0 and (arabic // (10 ** column)) % 10000 != 0:
                yield unit4[column // 4]
            if digit != 0:
                yield unit1[column % 4]
                yield digits[digit]
    return sign + ''.join(list(convert())[::-1])


def kanji_to_int(kanji):
    if not isinstance(kanji, str):
        return 'error'
    a0 = a1 = a4 = 0
    for j in kanji:
        if j in arabics:
            a0 = a0 * 10 + arabics[j]
        elif j in arabic1:
            a1 += (a0 or 1) * arabic1[j]
            a0 = 0
        elif j in arabic4:
            a4 += (a0 + a1 or 1) * arabic4[j]
            a0 = a1 = 0
        else:
            return 'error'
    return a0 + a1 + a4

    