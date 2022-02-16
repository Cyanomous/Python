
class Operators_and_Expressions:

    class Operators:
        # Plus(+)
        print(3 + 5)  # Gives 8
        print("a" + "b")  # Gives ab

        # Minus(-)
        # Gives 26, if first number is left blank it is assumed to be zero
        print(50 - 24)

        # Multiply(*)
        print(2 * 3)  # Gives 6
        print("la" * 3)  # Gives lalala

        # Power(**)
        print(3 ** 4)  # Gives 81 or 3 to the power of 4(3x3x3x3)

        # Divide(/)
        print(13 / 3)  # Gives 4.333333...

        # Divide and floor(//)
        print(13 // 3)  # Gives 4
        print(-13 // 3)  # Gives -5
        print(9 // 1.81)  # 4.0

        # Modulo(%)
        print(13 % 3)  # Gives 1
        print(-25.5 % 2.25)  # Gives 1.5

        # Left shift(<<)
        print(2 << 2)  # Gives 8

        # Right shift(>>)
        print(11 >> 1)  # Gives 5

        # Bit-wise AND(&)
        print(5 & 3)  # Gives 1

        # Bit-wise OR(|)
        print(5 | 3)  # Gives 7

        # Bit-wise XOR(^)
        print(5 ^ 3)  # Gives 6

        # Bit-wise invert(~)
        print(~5)  # Gives -6

        # Less than(<)
        print(5 < 3)  # Gives False
        print(3 < 5)  # Gives True

        # Grater than(>)
        print(5 > 3)  # Gives True

        # Less than or equal to(<=)
        print(3 <= 5)  # Gives True, note: you can't do =<

        # Greater than or equal to(>=)
        print(5 >= 3)  # Gives True, noteL you still can't do =>

        # Equal to(==)
        print(5 == 3)  # GIves False
        print(3 == 3)  # Gives True
