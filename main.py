def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celsius = float(input("Enter the tempature in Celsius:"))
    fahrenheit = (9/5)*celsius +32
    print(f"Fahrenheit: {fahrenheit:.2f}")
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
