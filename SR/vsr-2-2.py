def counter(text):
    left_bracket = 0
    right_bracket = 0
    for el in text:

        if el == "(":
            left_bracket += 1
            yield el

        if el == ")":
          right_bracket += 1
          yield el 
        
    print("Всего скобок: ", left_bracket + right_bracket)
    print("Левых: ", left_bracket)
    print("Правых: ", right_bracket)

    if left_bracket != right_bracket:
        print("Проверка на парность не пройдена")
    else:
        print("Проверка на парность пройдена")

words = input("Введите текст: \t\n")
con = counter(words)
try:
  while True:
    next(con)
except StopIteration:
  pass