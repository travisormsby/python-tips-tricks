# %%
coordinates = (2, 4, 5)
coordinates_dict = {
    "x": 2,
    "y": 4,
    "z": 5
}

def distance_from_origin(x, y, z):
    return (x**2 + y**2 + z**2) ** 0.5

x, y, z = coordinates_dict.values()

distance_from_origin(*coordinates_dict.values())


#%%
from typing import NamedTuple

class Tract(NamedTuple):
    population: int
    households: int

tract1 = Tract(3000, 1200)
tract2 = Tract(3500, 1300)
tract3 = Tract(2900, 1100)

tract1.population

#%%
rows = ("x,y,z", "2,4,5")
with open("data.csv", "w") as f:
    f.write("\n".join(rows))

#%%
rows = ("x,y,z", "2,4,5")
print("\n".join(rows))

#%%
tract3 = {
    "area": 100,
    "area_water": 100,
    "population": 0
}

def pop_density(tract):
    try:
        land_area = tract["area"] - tract["area_water"]
        return tract["population"] / land_area
    except (KeyError, TypeError):
        tract["area_water"] = 0
        return tract["population"] / land_area
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e)
    

pop_density(tract1)


#%%
# Performance and Memory!
data_list = [5, 6, 7, "eight"]

data_list.remove("eight")

data_list

# %%
data_tuple = (5, 6, 7, "eight")
# %%
import sys

print(sys.getsizeof(data_list))
print(sys.getsizeof(data_tuple))
# %%
data_tuple = (5, 6, 7, "eight")


def recaman_check(cur, i, visited):
    return (cur - i) < 0 or (cur - i) in visited

def recaman_list(n: int) -> list[int]:
    """
    return a list of the first n numbers of the Recaman series
    """

    visited_list = [0]
    current = 0
    for i in range(1, n):
        if recaman_check(current, i, visited_list):
            current += i
        else:
            current -= i
        visited_list.append(current)
    return visited_list

#%%
%%timeit -n 2 -r 2
recaman_list(1000000)
# %%

setExample = {0, 5, 7}

dictExample = {'first': 0,
'second': 5,
'third': 7}

def recaman_set(n: int):
    """
    return a set of the first n numbers of the Recaman series
    """

    visited_set = {0}
    current = 0
    for i in range(1, n):
        if recaman_check(current, i, visited_set):
            current += i
        else:
            current -= i
        visited_set.add(current)
    return visited_set
# %%
%%timeit -n 2 -r 2
recaman_set(1000000)
# %%
def someFunction(a,b):
    do some logic
    return someAnswer

def someGenerator(a,b):
    do some logic
    yield someAnswer

#%%
def massive_rf():
  """A regular function that produces even 
  numbers, endlessly."""
  x_list = []
  x = 0
  while True:
    x_list.append(x)
    x += 2

# Run it:
massive_rf()

#%%
def massive_gen():
  """A generator that produces even 
  numbers, endlessly."""
  x = 0
  while True:
    yield x
    x += 2

# Run it:
list[massive_gen()]
# %%
for x in massive_gen():
    print(x)

#%%
employeeDatabase = [
  {'lastName': 'Knope', 'rate': 72000, 'pay_class': 'annual'},
  {'lastName': 'Gergich', 'rate': 17, 'pay_class': 'hourly'},
  {'lastName': 'Ludgate', 'rate': 60000, 'pay_class': 'annual'},
  {'lastName': 'Swanson', 'rate': 'redacted', 'pay_class': 'redacted'},
  {'lastName': 'Haverford', 'rate': 52000, 'pay_class': 'annual'}
]

def hourly_rate(payments):
  """Function that returns each salaried worker's hourly rate."""
  hourlyRates = []
  for worker in payments:
    if worker.get('pay_class') == 'annual':
      hourly = worker['rate'] / 2080
      hourlyRates.append(hourly)
  return hourlyRates

hourly_rate(employeeDatabase)
# %%
salariesPerHour = sum(hourly_rate(employeeDatabase))
print(salariesPerHour)
# %%
def hourly_rate_gen(payments):
  """Generator that yields each salaried worker's 
  hourly rate."""
  for worker in payments:
    if worker.get('pay_class') == 'annual':
      hourly = worker['rate'] / 2080
      yield hourly

hourly_rate_gen(employeeDatabase)
# %%
sum(hourly_rate_gen(employeeDatabase))
# %%
print(sys.getsizeof(sum(hourly_rate(employeeDatabase))))
# %timeit sum(hourly_rate_gen(employeeDatabase))
# %%
