"""File that handles arithmetic operations"""

from text_process import Token

prec_map = {"-": 1, "+": 2, "*": 3, "/": 4, "(": 0}


def operate(arg1: float, arg2: float, opcode: str) -> float:
    """Perform operation specified by opcode"""
    match opcode:
        # Addition
        case "+":
            return arg1 + arg2
        # Subtraction
        case "-":
            return arg1 - arg2
        # Multiplication
        case "*":
            return arg1 * arg2
        # Division
        case "/":
            return arg1 / arg2
        # Unhandled operations
        case _:
            raise NotImplementedError(f"Unkown Opcode '{opcode}'")


def arith_eval(tkn_list: list[Token]) -> float:
    """Evaluate the expression using shunting yard algorithm"""
    # Generate RPN Expression
    rpn_stack = get_rpn(tkn_list)
    # Evaluate RPN expresison and return
    return rpn_eval(rpn_stack)


def get_rpn(tkn_list: list[Token]) -> list[Token]:
    """
    Rearrange elements of arithmetic expression into Reverse Polish Notation
    """
    rpn_stack: list[Token] = []
    op_stack: list[Token] = []
    # Shunting-Yard Algorithm
    for tkn in tkn_list:
        match tkn.type:
            # Add numbers to stack
            case "NUMBER":
                rpn_stack.append(tkn)
            # Process opcode
            case "OPCODE":
                while op_stack:
                    # Pop operators of high precedence so they come first
                    # Pop operators of same precedence for left assoc
                    if prec_map[op_stack[-1].value] >= prec_map[tkn.value]:
                        rpn_stack.append(op_stack.pop())
                    else:
                        break
                op_stack.append(tkn)
            # Handle paranthesis
            case "PAREN":
                if tkn.value == "(":
                    op_stack.append(tkn)
                else:
                    while op_stack[-1].type != "PAREN":
                        rpn_stack.append(op_stack.pop())
                    # Remove the left paren
                    op_stack.pop()
            case _:
                raise NotImplementedError(f"Unhandled Token {tkn.value}")

    # Add remaining operands
    while op_stack:
        rpn_stack.append(op_stack.pop())

    # Return expression in RPN
    return rpn_stack


def rpn_eval(rpn_stack: list[Token]) -> float:
    """Evaluate the RPN expression"""
    aux_stack: list[float] = []
    for tkn in rpn_stack:
        if tkn.type == "OPCODE":
            arg2 = aux_stack.pop()
            arg1 = aux_stack.pop()
            result = operate(arg1, arg2, tkn.value)
            aux_stack.append(result)
        else:
            aux_stack.append(float(tkn.value))

    return aux_stack[0]
