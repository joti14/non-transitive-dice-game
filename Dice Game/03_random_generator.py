import secrets
import hashlib

class RandomGenerator:
    def generate_secure_key(self):
        return secrets.token_bytes(32)  # Generate a 256-bit secure key

    def generate_random_number(self, range_max, key):
        value = secrets.randbelow(range_max + 1)  # Generate a random number in the range
        hmac = hashlib.sha3_256(key + str(value).encode()).hexdigest()  # Calculate HMAC
        return value, hmac  # Return the random number and its HMAC