class StringReverser:
    def __init__(self):
        self.input_string = ""

    def get_input(self):
        """Prompt the user to enter a sentence."""
        self.input_string = input("Enter a sentence to reverse: ")

    def reverse_words(self):
        """Reverse the words in the current sentence."""
        words = self.input_string.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

# Example usage
if __name__ == "__main__":
    reverser = StringReverser()
    reverser.get_input()
    print("Reversed String:", reverser.reverse_words())
