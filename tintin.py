def count_pass(scores):
  count = 0
  for score in scores:
    if check_pass(score):
      count += 1
  return count

def check_pass(score):
  if score >= 80:
    return True
  else:
    return False

scores = [82, 73, 52, 90, 48]
number_of_pass = count_pass(scores)

print(number_of_pass)