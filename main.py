import os
import hashlib
import pickle
import random
import subprocess
import yaml
import requests

SECRET_KEY = "my_super_secret_key_123456"

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def list_files(user_path: str) -> str:
    # User input directly concatenated into shell command
    cmd = f"ls -la {user_path}"
    return subprocess.getoutput(cmd)

def load_user_data(data: bytes):
    # Untrusted pickle loading
    return pickle.loads(data)

def read_file(filename: str) -> str:
    # No validation on filename
    with open(filename, "r") as f:
        return f.read()

def parse_yaml(data: str):
    # yaml.load without safe_load
    return yaml.load(data, Loader=yaml.Loader)

def generate_token() -> str:
    # random is not cryptographically secure
    return "".join(str(random.randint(0, 9)) for _ in range(16))
  
def fetch_internal_url(url: str):
    # User-controlled URL used in backend request
    return requests.get(url, timeout=5).text

def calculate(expression: str):
    # Remote code execution risk
    return eval(expression)

def save_file(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)
    # World-writable permission
    os.chmod(filename, 0o777)
