def main():
    random_value = float(input("Enter random value: "))
    boundary_value = float(input("Enter boundary value: "))

    if random_value < boundary_value:
        print("random value < boundary value")
    elif random_value / boundary_value > 3:
        print("random value is greater than boudary value by more than 3 times")
    elif random_value > boundary_value:
        print("random value > boundary value")


if __name__ == "__main__":
    main()
