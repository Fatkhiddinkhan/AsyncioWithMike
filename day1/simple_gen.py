# def fib(n):
#     x, y = 1, 2
#     for _ in range(n):
#         yield x
#         x, y = y, x + y
#
# generator = fib(1000)
# for number in generator:
#     print(number, end=", ")

def fib(n: int) -> list[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers

print(fib(1000))
