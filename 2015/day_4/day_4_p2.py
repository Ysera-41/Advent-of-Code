import hashlib

secret = "iwrupvqb"

i = 1
while True:
    hash_value = hashlib.md5((secret + str(i)).encode()).hexdigest()

    if hash_value.startswith("000000"):
        print("Resposta:", i)
        print("Hash:", hash_value)
        break

    i += 1
