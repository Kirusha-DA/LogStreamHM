def even_until_237(values):
    res = []
    for i in values:
        if i == 237:
            return res
        if i % 2 == 0:
            res.append(i)
    return res


def main():
    values = []
    n = int(input("Enter number of elements: "))
    for _ in range(0, n):
        value = int(input())
        values.append(value)

    print(f"Result: {even_until_237(values)}")


if __name__ == "__main__":
    main()
