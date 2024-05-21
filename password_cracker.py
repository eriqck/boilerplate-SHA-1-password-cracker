import hashlib

def crack_sha1_hash(hash, use_salts=False):
    def load_passwords():
        with open('top-10000-passwords.txt', 'r') as file:
            return [line.strip() for line in file]

    def load_salts():
        with open('known-salts.txt', 'r') as file:
            return [line.strip() for line in file]

    def sha1_hash(string):
        return hashlib.sha1(string.encode()).hexdigest()
    
    passwords = load_passwords()

    if use_salts:
        salts = load_salts()
        for password in passwords:
            for salt in salts:
                # Check salt + password
                if sha1_hash(salt + password) == hash:
                    return password
                # Check password + salt
                if sha1_hash(password + salt) == hash:
                    return password
    else:
        for password in passwords:
            if sha1_hash(password) == hash:
                return password

    return "PASSWORD NOT IN DATABASE"

# Example test cases
print(crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"))  # should return "sammy123"
print(crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e"))  # should return "abacab"
print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # should return "password"

# Example test cases with salts
print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True))  # should return "superman"
print(crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True))  # should return "q1w2e3r4t5"
print(crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True))  # should return "bubbles1"
