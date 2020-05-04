import copy
from itertools import cycle
from typing import List


class VigenereCipher:
    def __init__(self, keyword: str):
        self._keyword_char_codes = self._get_keyword_char_codes(keyword)
        self._tableau = self._get_tableau()

    def encrypt(self, plain_text: str) -> str:

        # Add the keyword row

        keyword_char_code_generator = cycle(self._keyword_char_codes)
        encrypted_text = ""

        for letter in plain_text.lower():
            if letter == " ":
                encrypted_text += " "
                continue

            plain_text_char_code = ord(letter)
            keyword_char_code = next(keyword_char_code_generator)

            encrypted_text_char_code = self._tableau[keyword_char_code - 97][
                plain_text_char_code - 97
            ]

            encrypted_text += chr(encrypted_text_char_code)

        return encrypted_text

    def decrypt(self, encrypted_text: str) -> str:
        decrypted_text = ""

        keyword_char_code_generator = cycle(self._keyword_char_codes)

        for letter in encrypted_text.lower():
            if letter == " ":
                decrypted_text += " "
                continue

            encrypted_text_char_code = ord(letter)
            keyword_char_code = next(keyword_char_code_generator)

            index = self._tableau[keyword_char_code - 97].index(
                encrypted_text_char_code
            )

            decrypted_text_char_code = self._tableau[0][index]
            decrypted_text += chr(decrypted_text_char_code)

        return decrypted_text

    @staticmethod
    def _get_keyword_char_codes(keyword: str) -> List[int]:
        keyword_char_codes: List[int] = []

        for letter in keyword:
            keyword_char_codes.append(ord(letter))

        return keyword_char_codes

    @staticmethod
    def _get_tableau() -> List[List[int]]:
        tableau: List[List[int]] = []

        for i in range(0, 26):
            if i == 0:
                tableau.append(list(range(ord("a"), ord("z") + 1)))
            else:
                deep_copy = copy.deepcopy(tableau[i - 1])
                to_shift = deep_copy.pop(0)
                deep_copy.append(to_shift)
                tableau.append(deep_copy)

        return tableau
