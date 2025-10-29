# test_mix.py

from mix_function import mix

test_cases = [
    ("A aaaa bb c", "& aaa bbb c d"),
    ("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"),
    ("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&"),
    ("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff"),
    ("abcde", "abcde"),
    ("hello world", "world hello"),
    ("aaaa bbbb ccc", "aa bbbb ccc ddd"),
    ("test one", "test two"),
    ("aaaaa bbb ccc d", "aa bbb cccc e"),
    ("xyz xyz xyz", "xxyy zz")
]

def run_tests():
    for i, (s1, s2) in enumerate(test_cases, 1):
        result = mix(s1, s2)
        print(f"Test {i}:\n  s1: {s1}\n  s2: {s2}\n  Output: {result}\n{'-'*50}")

if __name__ == "__main__":
    run_tests()

