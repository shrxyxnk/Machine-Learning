def find_s_algorithm(examples):
    hypothesis = ['0'] * (len(examples[0]) - 1)  # Initialize most specific hypothesis
    for example in examples:
        if example[-1] == 'Yes':  # Only consider positive examples
            for i in range(len(example) - 1):  # Exclude class label
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'
    return hypothesis

# Sample dataset: [Sky, AirTemp, Humidity, Wind, Water, Forecast, Target]
training_examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', 'Yes']
]

# Run Find-S algorithm
final_hypothesis = find_s_algorithm(training_examples)

# Print the result
print("The most specific hypothesis is:", final_hypothesis)
