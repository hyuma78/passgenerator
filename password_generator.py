import random
import string
import os

# ─────────────────────────────────────────────
#  DIZIONARI LINGUE
# ─────────────────────────────────────────────
LANG = {
    "IT": {
        "title"            : "GENERATORE DI PASSWORD",
        "pick_lang"        : "Seleziona lingua / Select language:\n  [1] Italiano\n  [2] English\nScelta: ",
        "invalid_lang"     : "  → Inserisci 1 o 2.",
        "which_chars"      : "Quali tipi di caratteri includere?\n",
        "lowercase"        : "  Minuscole (a-z)?              [s/n] → ",
        "uppercase"        : "  Maiuscole (A-Z)?              [s/n] → ",
        "digits"           : "  Numeri   (0-9)?               [s/n] → ",
        "special"          : "  Caratteri speciali (!@#$...)?  [s/n] → ",
        "ask_length"       : "Lunghezza della password (minimo 4): ",
        "ask_quantity"     : "Quante password generare?            ",
        "yes_tokens"       : ("s", "si", "sì"),
        "no_tokens"        : ("n", "no"),
        "invalid_yn"       : "  → Rispondi con 's' o 'n'.",
        "invalid_num"      : "  → Inserisci un numero valido.",
        "min_num"          : "  → Il numero deve essere almeno {min}.",
        "no_chars_warning" : "\n⚠️  Nessun tipo di carattere selezionato. Uso tutte le opzioni.\n",
        "min_len_forced"   : "  → Lunghezza minima impostata a {len} per includere tutte le categorie.\n",
        "generating"       : "  Generando {qty} password da {len} caratteri...\n",
        "saved_in"         : "\n✅ Password salvate in: {path}\n",
        "file_header"      : "Generazione {qty} password | Lunghezza: {len}",
    },
    "EN": {
        "title"            : "PASSWORD GENERATOR",
        "pick_lang"        : "Select language:\n  [1] Italiano\n  [2] English\nChoice: ",
        "invalid_lang"     : "  → Enter 1 or 2.",
        "which_chars"      : "Which character types to include?\n",
        "lowercase"        : "  Lowercase (a-z)?              [y/n] → ",
        "uppercase"        : "  Uppercase (A-Z)?              [y/n] → ",
        "digits"           : "  Digits    (0-9)?              [y/n] → ",
        "special"          : "  Special chars (!@#$...)?       [y/n] → ",
        "ask_length"       : "Password length (minimum 4): ",
        "ask_quantity"     : "How many passwords to generate? ",
        "yes_tokens"       : ("y", "yes"),
        "no_tokens"        : ("n", "no"),
        "invalid_yn"       : "  → Answer with 'y' or 'n'.",
        "invalid_num"      : "  → Enter a valid number.",
        "min_num"          : "  → The number must be at least {min}.",
        "no_chars_warning" : "\n⚠️  No character type selected. Using all options by default.\n",
        "min_len_forced"   : "  → Minimum length set to {len} to include all categories.\n",
        "generating"       : "  Generating {qty} passwords of {len} characters...\n",
        "saved_in"         : "\n✅ Passwords saved in: {path}\n",
        "file_header"      : "Generated {qty} passwords | Length: {len}",
    },
}


# ─────────────────────────────────────────────
#  SELEZIONE LINGUA
# ─────────────────────────────────────────────
def pick_language():
    prompt = LANG["IT"]["pick_lang"]   # bilingue per questa prima domanda
    while True:
        scelta = input(prompt).strip()
        if scelta == "1":
            return LANG["IT"]
        if scelta == "2":
            return LANG["EN"]
        print(LANG["IT"]["invalid_lang"])


# ─────────────────────────────────────────────
#  HELPER: SI / NO
# ─────────────────────────────────────────────
def ask_yes_no(domanda, t):
    while True:
        risposta = input(domanda).strip().lower()
        if risposta in t["yes_tokens"]:
            return True
        if risposta in t["no_tokens"]:
            return False
        print(t["invalid_yn"])


# ─────────────────────────────────────────────
#  HELPER: NUMERO
# ─────────────────────────────────────────────
def ask_number(domanda, t, minimo=1):
    while True:
        try:
            valore = int(input(domanda).strip())
            if valore >= minimo:
                return valore
            print(t["min_num"].format(min=minimo))
        except ValueError:
            print(t["invalid_num"])


# ─────────────────────────────────────────────
#  GENERAZIONE PASSWORD
# ─────────────────────────────────────────────
def generate_password(length, charset, t):
    if not charset:
        print(t["no_chars_warning"])
        charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Individua le categorie presenti nel charset
    categories = []
    for pool in (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation):
        if any(c in charset for c in pool):
            categories.append(pool)

    # Forza lunghezza minima se necessario
    if length < len(categories):
        length = len(categories)
        print(t["min_len_forced"].format(len=length))

    # Un carattere garantito per categoria + resto casuale
    pwd = [random.choice(cat) for cat in categories]
    pwd += random.choices(charset, k=length - len(pwd))
    random.shuffle(pwd)

    return "".join(pwd)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    # 1. Lingua
    t = pick_language()

    print("\n" + "=" * 45)
    print(f"      🔐  {t['title']}  🔐")
    print("=" * 45 + "\n")

    # 2. Tipi di carattere
    charset = ""
    print(t["which_chars"])
    if ask_yes_no(t["lowercase"], t):
        charset += string.ascii_lowercase
    if ask_yes_no(t["uppercase"], t):
        charset += string.ascii_uppercase
    if ask_yes_no(t["digits"], t):
        charset += string.digits
    if ask_yes_no(t["special"], t):
        charset += string.punctuation

    # 3. Lunghezza e quantità
    print()
    length   = ask_number(t["ask_length"],   t, minimo=4)
    quantity = ask_number(t["ask_quantity"],  t, minimo=1)

    # 4. Genera
    print("\n" + "-" * 45)
    print(t["generating"].format(qty=quantity, len=length))

    passwords = [generate_password(length, charset, t) for _ in range(quantity)]

    for i, pwd in enumerate(passwords, 1):
        print(f"  {i:>3}. {pwd}")

    # 5. Salva nella cartella dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path  = os.path.join(script_dir, "password_salvate.txt")

    with open(file_path, "a") as f:
        f.write(f"\n--- {t['file_header'].format(qty=quantity, len=length)} ---\n")
        for i, pwd in enumerate(passwords, 1):
            f.write(f"  {i}. {pwd}\n")

    print("-" * 45)
    print(t["saved_in"].format(path=file_path))


if __name__ == "__main__":
    main()