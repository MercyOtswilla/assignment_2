def main():
    base = int(input("Enter the base number: "))
    exponential = int(input("Enter the exponential number: "))
    results = 1
    for i in range(exponential):
        results = results * base
        print(results)

        
main()
