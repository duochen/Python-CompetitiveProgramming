def main():
    # Read inputs
    p1 = input()
    c1 = input()
    c2 = input()

    # Build ciphertext -> plaintext mapping
    mapping = {}
    for pt_char, ct_char in zip(p1, c1):
        mapping[ct_char] = pt_char

    # If exactly one mapping is missing, infer it
    all_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    if len(mapping) == 26:
        missing_ct = all_chars - set(mapping.keys())
        missing_pt = all_chars - set(mapping.values())
        if len(missing_ct) == 1 and len(missing_pt) == 1:
            ct = missing_ct.pop()
            pt = missing_pt.pop()
            mapping[ct] = pt

    # Decrypt the third line, using '.' for unknown mappings
    decrypted = []
    for ch in c2:
        decrypted.append(mapping.get(ch, '.'))
    print("".join(decrypted))


if __name__ == "__main__":
    main()
