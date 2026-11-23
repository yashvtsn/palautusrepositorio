import random

def sample_bit(p):
    return int(random.random() < p)

def generate():
    B = sample_bit(0.9)

    if B == 0:
        R = 0
    else: 
        R = sample_bit(0.9)

    if B == 0:
        I = 0
    else:
        I = sample_bit(0.95)

    G = sample_bit(0.95)

    if I == 1 and G == 1:
        S = sample_bit(0.99)
    else:
        S = 0

    if S == 0:
        M = 0
    else: 
        M = sample_bit(0.99)

    return [B, R, I, G, S, M]

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
    data, 0,
    {1: 1, 3: 1, 4: 0}
)

print("P(B | R, G, not S) =", p1)

p2 = estimate_probability(
    data, 4,
    {1: 1, 2: 1, 3: 1}
)

print("P(S | R, I, G)     =", p2)

p3 = estimate_probability(
    data, 4,
    {1: 0, 2: 1, 3: 1}
)

print("P(S | not R, I, G) =", p3)




