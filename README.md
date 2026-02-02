A simple command-line Python script that generates strong, customizable passwords and saves them to a local text file.

## Features

- **Bilingual interface** — choose between English and Italian at startup.
- **Fully customizable** — pick which character types to include: lowercase, uppercase, digits, and special characters.
- **Configurable length and quantity** — set how long each password should be and how many to generate in one go.
- **Guaranteed complexity** — at least one character from each selected category is always included, so the output is never weak by accident.
- **Persistent storage** — every batch of generated passwords is appended to `passwords.txt` in the same directory as the script, so previous generations are never overwritten.
- **Cross-platform** — works on Windows, Linux, and macOS with no extra dependencies.

## Requirements

- Python 3.6 or higher

## Usage

1. Clone or download the repository.
2. Open a terminal and navigate to the script's directory.
3. Run the script:

```bash
python password_generator.py
```

4. Follow the on-screen prompts:
   - Select your language (Italian or English).
   - Choose which character types to include.
   - Set the desired password length (minimum 4).
   - Set how many passwords you want to generate.

5. The generated passwords are displayed in the terminal and automatically saved to `passwords.txt`.