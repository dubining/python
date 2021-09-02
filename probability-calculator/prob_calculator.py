import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list(Counter(dict(kwargs)).elements())

  def draw(self, k):
    if (len(self.contents) <= k):
      return self.contents
    
    removedBalls = random.choices(self.contents, k=k)

    ballsCounter = Counter(self.contents)
    ballsCounter.subtract(Counter(removedBalls))
    self.contents = list(ballsCounter.elements())

    return removedBalls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  suc = 0
  for i in range(num_experiments):
    tempHat = copy.deepcopy(hat)
    exp = copy.deepcopy(expected_balls)
    balls = tempHat.draw(num_balls_drawn)
    for j in balls:
      exp.setdefault(j, 0)
      exp[j] -= 1
    if len(list(filter(lambda x: x > 0, exp.values()))) == 0:
      suc += 1
  return suc / num_experiments