"""https://www.codewars.com/kata/52a78825cdfc2cfc87000005"""

import re
from operator import add, mul, sub, truediv

OPERATORS = {'+': add, '-': sub, '*': mul, '/': truediv}

OPERATOR_P = r'[+\-*/]'  # Find operators +, -, *, /
NUMBER_P = r'-?\d*\.?\d+'  # Find integers and floats

DOUBLE_NEG_PATTERN = re.compile(fr'({OPERATOR_P}|^)--')  # Use to replace double negations like --5+--3 with 5+3
PARENTHESES_PATTERN = re.compile(r'\(([^()]*)\)')  # Find content inside innermost parentheses
BIN_OPERATOR_PATTERN = re.compile(
    fr'(?<=\d)({OPERATOR_P})')  # Find operators. Excludes unary '-' and assumes parentheses have been removed.
MUL_DIV_PATTERN = re.compile(fr'(?<!\d){NUMBER_P}(?:[*/]{NUMBER_P})+')  # Find multiplication and division expressions


def calc(expression: str):
    expression = expression.replace(' ', '')
    return float(eval_expr(expression))


def eval_expr(expression: str) -> str:
    while paren_matches := PARENTHESES_PATTERN.findall(expression):
        for paren_match in paren_matches:
            expression = expression.replace(f'({paren_match})', eval_expr(paren_match))

    expression = DOUBLE_NEG_PATTERN.sub(r'\1', expression)
    operators = BIN_OPERATOR_PATTERN.findall(expression)

    # If there are operators of different precedence, split the expression into sub-expressions and evaluate them separately
    if ('+' in operators or '-' in operators) and ('*' in operators or '/' in operators):
        sub_expressions = MUL_DIV_PATTERN.findall(expression)
        for sub_expr in sub_expressions:
            expression = expression.replace(sub_expr, eval_expr(sub_expr))

    # At this point, all operators in the expression have the same precedence, so we can evaluate it from left to right
    components = BIN_OPERATOR_PATTERN.split(expression)  # Split the expression to operands and operators
    result = float(components[0])

    for i in range(1, len(components), 2):
        operator, operand = components[i:i + 2]
        result = OPERATORS[operator](result, float(operand))  # Equivalent to result = result {operator} operand

    return str(result)
