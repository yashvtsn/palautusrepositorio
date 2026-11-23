import random

def sample_bit(p):
    return int(random.random() < p)

def generate():
    E = sample_bit(1/111)
    B = sample_bit(1/365)

    if E == 0 and B == 0:
        A = sample_bit(0.0095)
    elif E == 0 and B == 1:
        A = sample_bit(0.92)
    elif E == 1 and B == 0:
        A = sample_bit(0.81)
    elif E == 1 and B == 1:
        A = sample_bit(0.97)

    return [E, B, A]

def generate_data(n):
    return [generate() for _ in range(n)]

data = generate_data(100000)

def estimate_probability(data, target, conditions):

    matching = [
        row for row in data
        if all(row[i] == value
               for i, value in conditions.items())
    ]

    if len(matching) == 0:
        return None

    positive = sum(row[target] for row in matching)

    return positive / len(matching)

p1 = estimate_probability(
    data,
    target=1,
    conditions={2: 1}
)

print(p1)

p2 = estimate_probability(
    data,
    target=1,
    conditions={2: 1, 0: 1}
)

print(p2)