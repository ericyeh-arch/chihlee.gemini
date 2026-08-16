"""終端機計算機。

執行方式：uv run 0802/calculator.py
"""

import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def calculate(expression: str) -> int | float:
    """只計算數字、四則運算與括號，拒絕執行任何 Python 程式碼。"""
    tree = ast.parse(expression, mode="eval")

    def evaluate(node: ast.AST) -> int | float:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.left), evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.operand))
        raise ValueError("只支援數字、+、-、*、/、//、%、** 與括號")

    return evaluate(tree.body)


def main() -> None:
    print("=== 計算機 ===")
    print("可用：+  -  *  /  //  %  **  與括號")
    print("輸入 exit 或 quit 結束\n")

    while True:
        try:
            expression = input("算式：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再見！")
            break

        if expression.lower() in {"exit", "quit"}:
            print("再見！")
            break
        if not expression:
            continue

        try:
            print(f"結果：{calculate(expression)}\n")
        except (SyntaxError, ValueError, ZeroDivisionError, OverflowError) as error:
            print(f"無法計算：{error}\n")


if __name__ == "__main__":
    main()
