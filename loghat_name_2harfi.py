def find_last_char(n):

    def generate_sequence():
        seq = []
        for i in range(1, 26):
            for j in range(1, i + 1):
                seq.append(''.join(map(lambda x: chr(ord('A') + x), range(i))))
        return seq

    sequence = generate_sequence()

    sequence.sort(key=lambda x: (len(x), x))

    return sequence[n - 1][-1]

print(find_last_char(100))  # Output: 'A'
