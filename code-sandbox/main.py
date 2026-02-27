
def generate_token() -> str:
    import secrets

    # PRECOGS_FIX: use the cryptographically secure secrets module for token generation
    return secrets.token_hex(8)