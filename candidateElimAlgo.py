def more_general(h1, h2):
    for x, y in zip(h1, h2):
        if x != '?' and (x != y and y != '?'):
            return False
    return True

def candidate_elimination_algorithm(examples):
    n_attributes = len(examples[0]) - 1
    S = examples[0][:-1]  # Initialize S with first positive example
    G = [['?' for _ in range(n_attributes)]]  # Most general hypothesis

    for example in examples:
        instance, label = example[:-1], example[-1]

        if label == 'Yes':  # Positive example
            # Remove inconsistent hypotheses from G
            G = [g for g in G if more_general(g, instance)]

            for i in range(n_attributes):
                if S[i] != instance[i]:
                    S[i] = '?'
        else:  # Negative example
            G_new = []
            for g in G:
                if more_general(g, instance):
                    for i in range(n_attributes):
                        if g[i] == '?':
                            if S[i] != instance[i]:
                                new_hypo = g.copy()
                                new_hypo[i] = S[i]
                                if new_hypo not in G_new:
                                    G_new.append(new_hypo)
            G = G_new

    return S, G

# Sample dataset: [Sky, AirTemp, Humidity, Wind, Water, Forecast, Target]
training_examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', 'Yes']
]

# Run Candidate Elimination
S_final, G_final = candidate_elimination_algorithm(training_examples)

# Print results
print("Final Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)
