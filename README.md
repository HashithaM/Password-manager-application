# Educational Password Manager

A Tkinter learning project that generates passwords and stores website login records in a local JSON file. It demonstrates desktop forms, clipboard integration, JSON updates, and record lookup.

> [!CAUTION]
> This implementation stores passwords in plaintext and uses Python's non-cryptographic `random` module. It is not safe for real credentials. The repository also contains credential-like sample data that should be treated as exposed: rotate any real passwords, remove the data files from public source and history, and never reuse the included values.

## Features

- Password generation from letters, numbers, and symbols
- Clipboard copy with `pyperclip`
- Local JSON save and update flow
- Website-based credential lookup
- Tkinter desktop interface

## Requirements

```bash
pip install pyperclip
```

## Run

```bash
python main.py
```

## Security improvements needed

- Generate credentials with Python's `secrets` module.
- Store secrets in the operating system's credential vault or use authenticated encryption with a separately protected key.
- Add runtime data files such as `data.json` and `data.txt` to `.gitignore`.
- Do not display stored passwords in plaintext.

Use this repository only as a GUI/JSON exercise until those controls are implemented.
