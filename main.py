from TempMem import *

def main():
    memory = MemoryBank(input("What Tier is your party? (Pg 24): "), input("How many characters are in your party?: "), input("Is this Combat Scene Easy, Medium, or Hard?: "))
    memory.ValidityCheck()
    memory.log()


if __name__ == "__main__":
    main()
