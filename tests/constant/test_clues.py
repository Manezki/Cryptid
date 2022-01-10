import unittest

from cryptidsolver.constant.clues import by_booklet_entry

class TestClueLookup(unittest.TestCase):

    # Number 2 is non-inverted clue for every alphabet

    def test_rejects_incorrect_alphabet(self) -> None:
        with self.assertRaises(AssertionError, msg="Should only accept alphabets in ['alpha', 'beta', 'gamma', 'delta', 'epsilon']"):
            by_booklet_entry("A", 2)


    def test_rejects_incorrect_number(self) -> None:

        for number in [-1, 0, 97]:
            with self.assertRaises(AssertionError, msg="Should only accept numbers in range 1...96"):
                by_booklet_entry("alpha", number)


    def test_accepts_proper_alphabets(self) -> None:

        alphabets = ["alpha", "beta", "gamma", "delta", "epsilon"]

        for alpha in alphabets:
            try:
                by_booklet_entry(alpha, 2)
            except Exception:
                self.fail("Proper alphabet {} was not accepted".format(alpha))


    def test_accepts_proper_number_as_argument(self) -> None:

        for number in range(1, 97, 1):
            try:
                by_booklet_entry("alpha", number)
            except Exception as e:
                if (type(e).__name__ == "AssertionError") and ("Number should in range" in str(e)):
                    self.fail("Proper number {} was not accepted".format(number))


    def test_fails_on_inverted_clues(self) -> None:

        with self.assertRaises(NotImplementedError, msg="Should fail on inverted clues"):
            # Epsilon 4 is clue: 'not_forest/mountain'
            by_booklet_entry("epsilon", 4)


if __name__ == "__main__":
    unittest.main()
