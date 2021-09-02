import math

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description=''):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    if (not self.check_funds(amount)):
      return False
    self.balance -= amount
    self.ledger.append({"amount": -amount, "description": description})
    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, cat):
    if (not self.withdraw(amount, 'Transfer to ' + cat.name)):
      return False
    cat.deposit(amount, 'Transfer from ' + self.name)
    return True

  def check_funds(self, amount):
    return self.balance >= amount

  def __str__(self):
    result = ''
    starsNum = 30 - len(self.name)
    result += '*'*(starsNum // 2) + self.name + '*'*(starsNum // 2 + starsNum % 2) + '\n'

    for op in self.ledger:
      formatDesc = op["description"] + ' ' * 23
      formatDesc = formatDesc[:23]

      formatAmount = ' ' * 7 + format(op["amount"], '.2f')
      formatAmount = formatAmount[-7:]
      result += (formatDesc+formatAmount) + '\n'

    result += 'Total: ' + format(self.balance, '.2f')

    return result


def create_spend_chart(categories):
  result = ''
  spendData = []
  for cat in categories:
    spendData.append([cat.name, -sum(list(map(lambda x: x['amount'], filter(lambda x: x['amount'] < 0, cat.ledger))))])

  totalSpend = sum(list(map(lambda x: x[1], spendData)))

  result += 'Percentage spent by category\n'

  for i in range(100, -1, -10):
    result += (' ' * 3 + str(i))[-3:] + '|'
    for catData in spendData:
      if math.floor(catData[1] / totalSpend * 100) >= i:
        result += ' o '
      else:
        result += ' ' * 3
    result += ' \n'
  result += ' ' * 4 + '-' * (len(spendData) * 3 + 1) + '\n'

  for i in range(max(list(map(lambda x: len(x[0]), spendData)))):
    result += ' ' * 4
    for catData in spendData:
      if i < len(catData[0]):
        result += ' ' + catData[0][i] + ' '
      else:
        result += ' ' * 3
    result += ' \n'

  return result[:-1]