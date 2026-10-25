# Secure Desktop Password Manager

A Tkinter learning project that generates strong passwords and stores login records in the operating system's credential vault instead of plaintext repository files.

## Security design

- Passwords are generated with Python's cryptographically secure `secrets` module.
- Email and password records are stored through `keyring` using the operating system's credential backend.
- Retrieved passwords are copied to the clipboard instead of displayed in a dialog.
- Runtime credential files are ignored by Git.
- `example-data.json` contains unmistakable dummy values for historical-format reference only; the application does not read it.

> [!IMPORTANT]
> Any password that appeared in an earlier public revision must still be rotated. Replacing current files does not invalidate a credential or erase Git history.

## Requirements

```bash
pip install -r requirements.txt
```

The application requires a working secure `keyring` backend. It fails visibly if the operating system cannot provide one and never falls back to plaintext storage.

## Run

```bash
python main.py
```

Enter a website, username or email, and password. Saving writes the record to the OS credential vault. Searching by the same website copies the password to the clipboard.
