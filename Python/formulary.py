# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:16:48 2024

@author: Florian Bethe
"""
## general

#   Konsole clearen
#       https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
#       https://hellocoding.de/blog/coding-language/python/farben-im-terminal
print("\033[H\033[J", end="")       


ZEICHEN = " ─ │ ┌ ┐ └ ┘ ├ ┤ ┬  ┴  ┼ ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╫ ╬ ╪ █ "


# ___________________________________________________________________________ #
## colorama
# Bibliothek importieren
import colorama
"""
    # requitements.txt
    print(f"colorama=={colorama.__version__}")
"""

colorama.init(autoreset=True)

FORMAT = {
    "RESET":      "\033[0m",

    "BOLD":       "\033[1m",
    "UNDERLINE":  "\033[4m",

    "FG_SCHWARZ": "\033[30m",
    "FG_ROT":     "\033[31m",
    "FG_GRÜN":    "\033[32m",
    "FG_GELB":    "\033[33m",
    "FG_BLAU":    "\033[34m",
    "FG_PINK":    "\033[35m",
    "FG_TÜRKIS":  "\033[36m",
    "FG_GRAU":    "\033[37m",

    "BG_SCHWARZ": "\033[40m",
    "BG_ROT":     "\033[41m",
    "BG_GRÜN":    "\033[42m",
    "BG_GELB":    "\033[43m",
    "BG_BLAU":    "\033[44m",
    "BG_PINK":    "\033[45m",
    "BG_TÜRKIS":  "\033[46m",
    "BG_GRAU":    "\033[47m",

    "GRÜN_AUF_GRAU":  "\033[32;47m"}

colorama.deinit()

# ___________________________________________________________________________ #


#### Machine Learning (ML)

## sklearn
# pip install scikit-learn


#### Zufallszahlen und Cryptografie

## cryptography
# pip install cryptography

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_chacha20_random_bytes(num_bytes):
    # Generiere einen zufälligen 256-bit Schlüssel
    key = os.urandom(32)
    # Generiere einen zufälligen 96-bit Nonce
    nonce = os.urandom(12)
    
    # Erstelle eine ChaCha20-Instanz
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None)
    
    # Erstelle einen Encryptor
    encryptor = cipher.encryptor()
    
    # Generiere Zufallsbytes
    random_bytes = encryptor.update(b'\x00' * num_bytes)
    
    return random_bytes

# Beispiel: Generiere 16 zufällige Bytes
random_data = generate_chacha20_random_bytes(16)
print("Zufällige Bytes:", random_data.hex())

# Konvertiere zu einer Ganzzahl
random_int = int.from_bytes(random_data, byteorder='big')
print("Zufällige Ganzzahl:", random_int)

# Generiere eine Zufallszahl zwischen 0 und 1
random_float = random_int / (2**(8*len(random_data)) - 1)
print("Zufällige Gleitkommazahl zwischen 0 und 1:", random_float)



## cpuinfo
# Echte Zufallszahlen via Intel Hardware
# pip install py-cpuinfo
import cpuinfo
# Prüfen, ob der Prozessor RDRAND unterstützt
print("RDRAND supported:", "rdrand" in cpuinfo.get_cpu_info()["flags"])