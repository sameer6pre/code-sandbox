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
    cmd = f"ls -la {user_path}"
    return subprocess.getoutput(cmd)

def load_user_data(data: bytes):
    return pickle.loads(data)

def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()

def parse_yaml(data: str):
    return yaml.load(data, Loader=yaml.Loader)

def generate_token() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(16))
  
def fetch_internal_url(url: str):
    return requests.get(url, timeout=5).text

def calculate(expression: str):
    return eval(expression)

def save_file(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)
    os.chmod(filename, 0o777)
