import cohere
co = cohere.Client('O4y6PQNUhTwWeN7js5W4890dF8xUrZ6Z0oX8ng8Q') # This is your trial API key
response = co.generate(
  model='command',
  prompt='{prompt}',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))