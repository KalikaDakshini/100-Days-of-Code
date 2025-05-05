"""Main File of the calculator."""

from text_process import tokenize
from arith import arith_eval


def repl():
    """REPL for calculator"""
    while True:
        try:
            # 1. Read from prompt
            expr_str = input(">> ")
            # 2. Evaluate Prompt
            tkn_list = tokenize(expr_str)
            result = arith_eval(tkn_list)
            # 3. Print Result
            print(result)

        except EOFError:
            print("\nExiting")
            break

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            continue


if __name__ == "__main__":
    repl()
