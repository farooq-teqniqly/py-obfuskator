from unittest import TestCase
from pyobfuskator.ciphers.vigenerecipher import VigenereCipher


class VigenereCipherTests(TestCase):
    def test_encrypt_encrypts_string(self):
        # Arrange
        cipher = VigenereCipher(keyword="petulant")
        plain_text = "The quick brown for jumped over the lazy dog"

        # Act
        encrypted_text = cipher.encrypt(plain_text)

        # Assert
        self.assertNotEqual(encrypted_text.lower(), plain_text.lower())

    def test_decrypt_decrypts_string(self):
        # Arrange
        cipher = VigenereCipher(keyword="petulant")
        plain_text = "The quick brown for jumped over the lazy dog"

        # Act
        decrypted_text = cipher.decrypt(cipher.encrypt(plain_text))

        # Assert
        self.assertEqual(decrypted_text.lower(), plain_text.lower())
