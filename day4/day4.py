import hashlib


def get_lowest_hash(secret, zero_count):
    zero_string = "0" * zero_count
    i = 0

    while True:
        i += 1
        attempt_hash = hashlib.md5((secret + str(i)).encode('utf-8')).hexdigest()

        if attempt_hash[:zero_count] == zero_string:
            return i


secret_key = "iwrupvqb"
print("Part 1: Lowest hash for 5 zeroes is %d" % get_lowest_hash(secret_key, 5))
print("Part 2: Lowest hash for 6 zeroes is %d" % get_lowest_hash(secret_key, 6))
