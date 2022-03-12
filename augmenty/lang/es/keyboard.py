from ...util import registry


@registry.keyboards("es_qwerty.v1")
def create_qwerty_es():
    return {
        "default": [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "´", "`"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ", ";", "'"],
            ["<", "z", "x", "c", "v", "b", "n", "m", ",", ".", "ç"],
        ],
        "shift": [
            ["¡", "!", "#", "$", "%", "/", "&", "*", "(", ")", "_", "+"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "º", "¨"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", ":", '"'],
            [">", "Z", "X", "C", "V", "B", "N", "M", "¿", "?", "Ç"],
        ],
    }
