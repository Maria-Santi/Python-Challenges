def fizz_buzz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


for i in range(1, 16):
    print(fizz_buzz(i))
