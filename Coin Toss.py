import CoinClass as c
# ****this is not the name of the class, the name of the FILE with an alias

# The main function.


def main():
    # Create an object from the Coin class.
    # *********this creates an instance called 'my_coin' of the class 'Coin()'
    my_coin = c.Coin()

    # Display the side of the coin that is facing up.
    # notice you do not have to supply the argument/parameter
    print('This side is up:', my_coin.get_sideup())
    # will return heads becauase you initialized an instance with
    # the attribute "sideup" which is already set to heads
    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()  # calls the toss method

        # using the __ on the attribute hides it, so the following line is not read by the interpreter
        my_coin.sideup = 'Heads'

        # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())


# Call the main function.
main()
