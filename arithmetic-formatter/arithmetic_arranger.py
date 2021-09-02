from functools import reduce

def arithmetic_arranger(problems, ans=False):
  if (len(problems) > 5):
    return 'Error: Too many problems.'

  arranged_problems = ''

  problems = list(map(lambda x: x.split(' '), problems))

  if (len(list(filter(lambda x: x[1] != '+' and x[1] != '-', problems))) > 0):
    return "Error: Operator must be '+' or '-'."

  if (not reduce(lambda a, b: bool(a and b), map(lambda x: bool(x[0].isnumeric() and x[2].isnumeric()), problems))):
    return "Error: Numbers must only contain digits."

  if (not reduce(lambda a, b: bool(a and b), map(lambda x: bool(len(x[0]) < 5 and len(x[2]) < 5), problems))):
    return "Error: Numbers cannot be more than four digits."

  maxLen = list(
      map(
        lambda x: max(len(x[0]), len(x[2])), problems
      )
    )

  for i in range(len(problems)):
    arranged_problems += ' ' * (2 + maxLen[i] - len(problems[i][0])) + problems[i][0] + ' ' * 4
  arranged_problems = arranged_problems[:-4] + '\n'

  for i in range(len(problems)):
    arranged_problems += problems[i][1] + ' ' * (1 + maxLen[i] - len(problems[i][2])) + problems[i][2] + ' ' * 4
  arranged_problems = arranged_problems[:-4] + '\n'

  for i in range(len(problems)):
    arranged_problems += '-' * (2 + maxLen[i]) + ' ' * 4
  arranged_problems = arranged_problems[:-4]

  if ans:
    arranged_problems += '\n'
    for i in range(len(problems)):
      result = 0
      if problems[i][1] == '+':
        result = int(problems[i][0]) + int(problems[i][2])
      else:
        result = int(problems[i][0]) - int(problems[i][2])
      arranged_problems += ' ' * (2 + maxLen[i] - len(str(result))) + str(result) + ' ' * 4
    arranged_problems = arranged_problems[:-4]

  return arranged_problems