from calculator import Calculator
from gui import Mygui

def main():
    gui = Mygui(None)
    calculator = Calculator(gui)
    gui.calculator = calculator
    gui.run_root()

if __name__ == "__main__":
    main()