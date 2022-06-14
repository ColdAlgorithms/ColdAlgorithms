def is_odd(x):
    """Returns True if x is odd and False if x is even"""
    return x % 2 == 1         # The % operator returns the remainder of integer division


def main():
  # Test function main picks up odd number in the given list.
  print(list(filter(is_odd, [1, 4, 5, 9, 10])))

if __name__ == "__main__":
    main()
