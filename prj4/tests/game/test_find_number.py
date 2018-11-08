from game.find_number import FindNumberGame, Way


def test_should_return_bigger_if_secret_number_is_bigger():
    """
        Test game return BIGGER if the secret number is bigger
    """
    secret_number = 54
    game = FindNumberGame(secret_number)

    # Try with a smaller number
    res = game.try_number(12)

    assert res == Way.BIGGER


def test_should_return_smaller_if_secret_number_is_smaller():
    """
        Test game return SMALLER if the secret number is smaller
    """
    secret_number = 10
    game = FindNumberGame(secret_number)

    # Try with a bigger number
    res = game.try_number(12)

    assert res == Way.SMALLER


def test_should_return_equals_if_secret_number_is_equal():
    """
        Test game return EQUAL if the secret number is equal
    """
    secret_number = 10
    game = FindNumberGame(secret_number)

    # Try with a smaller number
    res = game.try_number(10)

    assert res == Way.EQUAL
