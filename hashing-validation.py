# Organization-based contract signing and authentication system
import hashlib
import json
import uuid
import time

class AuthSystem:
    def __init__(self):
        self.records = {}

    def store(self, key, value):
        self.records[key] = value

    def retrieve(self, key):
        return self.records.get(key)

def build_contract(org, approver, detail):
    return {
        "id": str(uuid.uuid4()),
        "organization": org,
        "approver": approver,
        "detail": detail,
        "created": time.time()
    }

def encode(contract):
    return json.dumps(contract, sort_keys=True)

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def sign(hash_value, secret):
    return hashlib.sha256(f"{hash_value}:{secret}".encode()).hexdigest()

def verify(hash_value, signature, secret):
    return sign(hash_value, secret) == signature

def process():
    system = AuthSystem()

    contract = build_contract("OrgX", "LeadAdmin", "Security Policy Agreement")
    encoded = encode(contract)
    h = hash_data(encoded)

    system.store(h, contract)

    signature = sign(h, "auth_key_777")
    valid = verify(h, signature, "auth_key_777")

    print("Hash:", h)
    print("Signature:", signature)
    print("Valid:", valid)

    return system

def audit(system):
    print("\nStored Contracts:")
    for k, v in system.records.items():
        print(k, v)

def status():
    print("\nSystem Status: Active Authentication Layer")

def main():
    sys = process()
    audit(sys)
    status()
    print("Complete")

if __name__ == "__main__":
    main()
