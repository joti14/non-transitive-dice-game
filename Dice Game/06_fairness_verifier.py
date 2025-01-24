import hashlib

class FairnessVerifier:
    def verify_hmac(self, value, key, hmac):
        expected_hmac = hashlib.sha3_256(key + str(value).encode()).hexdigest()
        return hmac == expected_hmac  # Check if the HMAC matches