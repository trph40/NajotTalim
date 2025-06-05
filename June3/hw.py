from collections import namedtuple
from math import sqrt

### 1
Car = namedtuple('Car', ['model', 'year', 'price'])
cars = [
    Car('Nexia', 2018, 8000),
    Car('Malibu', 2020, 25000),
    Car('Spark', 2019, 6000)
]
expensive = max(cars, key=lambda c: c.price)
print("Eng qimmat mashina:", expensive)

### 2
Student = namedtuple('Student', ['name', 'age', 'grades'])
students = [
    Student('Ali', 20, [4, 5, 3]),
    Student('Vali', 21, [5, 5, 4]),
    Student('Gulbahor', 19, [3, 4, 3]),
    Student('Aziza', 22, [4, 4, 4]),
    Student('Kamol', 20, [5, 5, 5])
]
print("Talabalar o‘rtacha baholari:")
for s in students:
    avg = sum(s.grades) / len(s.grades)
    print(f"{s.name}: {avg}")

### 3
Color = namedtuple('Color', ['r', 'g', 'b'])
c1 = Color(100, 150, 200)
c2 = Color(50, 100, 50)
new_color = Color(c1.r + c2.r, c1.g + c2.g, c1.b + c2.b)
print("Yangi rang:", new_color)

###4
Product = namedtuple('Product', ['name', 'quantity', 'price'])
products = [
    Product('Olma', 3, 5000),
    Product('Banan', 2, 8000),
    Product('Shaftoli', 1, 10000),
    Product('Anor', 5, 4000)
]
total = sum(p.quantity * p.price for p in products)
print("Umumiy summa:", total)

### 5
Point = namedtuple('Point', ['lat', 'lon'])
p1 = Point(2, 3)
p2 = Point(7, 8)
distance = sqrt((p2.lat - p1.lat)**2 + (p2.lon - p1.lon)**2)
print("Masofa:", distance)

### 6
Time = namedtuple('Time', ['h', 'm', 's'])
t1 = Time(1, 20, 15)
t2 = Time(2, 45, 50)
total_sec = t1.h*3600 + t1.m*60 + t1.s + t2.h*3600 + t2.m*60 + t2.s
h = total_sec // 3600
m = (total_sec % 3600) // 60
s = total_sec % 60
print(f"Yig‘indi vaqt: {h}:{m}:{s}")

### 7
Animal = namedtuple('Animal', ['name', 'species', 'age'])
animals = [
    Animal('Leo', 'Lion', 5),
    Animal('Mikki', 'Mouse', 2),
    Animal('Sharik', 'Dog', 4),
    Animal('Mittens', 'Cat', 1),
    Animal('Donkey', 'Horse', 3)
]
sorted_animals = sorted(animals, key=lambda a: a.age)
print("Hayvonlar yosh bo‘yicha:")
for a in sorted_animals:
    print(a)

### 8
BankAccount = namedtuple('BankAccount', ['owner', 'balance'])
accounts = [
    BankAccount('Ali', 2000),
    BankAccount('Vali', 3500),
    BankAccount('Olim', 1500)
]
richest = max(accounts, key=lambda a: a.balance)
print("Eng boy:", richest)

### 9
Movie = namedtuple('Movie', ['title', 'director', 'year'])
movies = [
    Movie('Titanic', 'James Cameron', 1997),
    Movie('Avatar', 'James Cameron', 2009),
    Movie('Inception', 'Christopher Nolan', 2010)
]
after_2000 = [m for m in movies if m.year > 2000]
print("2000-yildan keyingi filmlar:")
for m in after_2000:
    print(m)

### 10
Computer = namedtuple('Computer', ['brand', 'ram', 'cpu'])
pcs = [
    Computer('HP', 8, 2.5),
    Computer('Dell', 16, 3.1),
    Computer('Lenovo', 8, 2.8),
    Computer('Acer', 16, 3.5)
]
fastest = max(pcs, key=lambda c: c.cpu)
print("Eng kuchli CPU:", fastest)

### 11
def solution(s):
    return s.upper()


### 12
def correct_polish_letters(st):
    table = {
        'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l',
        'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'
    }
    return ''.join(table.get(ch, ch) for ch in st)

### 13
def build_string(*args):
    return "I like {}!".format(", ".join(args))

### 14
def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"

### 15
def count_char_occurrences(strng, char):
    return strng.count(char)