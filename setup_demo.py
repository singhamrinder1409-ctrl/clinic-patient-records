"""Create synthetic accounts for local coursework tests. No real records are included."""
from pathlib import Path
import hashlib

accounts = {"user": "123456", "ali": "@G00dPassw0rd"}
Path("clinic/records").mkdir(parents=True, exist_ok=True)
target = Path("clinic/users.txt")
if target.exists():
    print("Existing local account file retained.")
else:
    target.write_text("".join(f"{name},{hashlib.sha256(password.encode()).hexdigest()}\n" for name, password in accounts.items()))
    print("Synthetic demo accounts created.")
