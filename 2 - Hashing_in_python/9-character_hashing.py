s = ["azyxyyzaaaa"]
q = ["d", "a", "y", "x"]

# Initialize frequency list for 26 lowercase letters (a–z)
hash_list = [0] * 26

def char_hashing():
    # Loop through each character in the string
    for char in s[0]:  # s[0] because s is a list with one string
        index = ord(char) - 97  # 'a' -> 0, ..., 'z' -> 25
        hash_list[index] += 1

    # Lookup frequency for each query character
    for char in q:
        index = ord(char) - 97
        print(f"'{char}' : {hash_list[index]}")

char_hashing()
