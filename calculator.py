def show_banner():
    print(r"""
    ╔══════════════════════════════════════╗
    ║        👻  CALCULATOR MASTER  👻      ║
    ║     ~ a hauntingly good calculator ~  ║
    ╚══════════════════════════════════════╝
    """)


def show_menu():
    print("┌────────────────────────────┐")
    print("│  1. Addition               │")
    print("│  2. Subtraction            │")
    print("│  3. Multiplication         │")
    print("│  4. Division               │")
    print("│  5. Exit                   │")
    print("└────────────────────────────┘")


def show_result(op_symbol, a, b, result):
    print("\n  ✨ ─────────────────────── ✨")
    print(f"    {a} {op_symbol} {b}  =  {result}")
    print("  ✨ ─────────────────────── ✨\n")
 
def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("⚠️ Invalid input. Please enter numeric values only.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b


def main():
    show_banner()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("\n👋 The spirits bid you farewell. Goodbye!\n")
            break
        elif choice not in ("1", "2", "3", "4"):
            print("⚠️ Invalid choice. Please select 1-5.")
            continue

        a, b = get_numbers()

        if choice == "1":
            show_result("+", a, b, add(a, b))
        elif choice == "2":
            show_result("-", a, b, subtract(a, b))
        elif choice == "3":
            show_result("*", a, b, multiply(a, b))

if __name__ == "__main__":
    main()