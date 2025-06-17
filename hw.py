## 1
def multi_table(number):
    result = ''
    for i in range(1, 11):
        result += f"{i} * {number} = {i * number}\n"
    return result.rstrip()


## 2
def who_is_paying(name):
    if len(name) <= 2:
        return [name]
    return [name, name[:2]]

## 3
def name_shuffler(str_):
    first, last = str_.split()
    return f"{last} {first}"    

## 4
def contamination(text, char):
    if not text or not char:
        return ''
    return char * len(text)

## 5
def no_space(x):
    return x.replace(" ", "")

## 6
def format_money(amount):
    return "$%.2f" % amount

## 7
def billboard(name, price=30):
    total = 0
    for letter in name:
        total += price
    return total

## 8
def is_uppercase(inp):
    return inp.upper() == inp

## 9
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[1] > scores[0]:
        return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
    else:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."
    

## 10
def is_loch_ness_monster(string):
    return "3.50" in string or "tree fiddy" in string or "three fifty" in string