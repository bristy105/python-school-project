# Import the randint function from the random module to be used in the feed_the_cat
# function.
from random import randint

class Cat:
    """
    A mutable class that models a cat on a very general level.
    """

    def __init__(self, weight, mood):
        """Constructor that initializes the weight and mood of a cat object.
        Raises an exception, if one or both of the parameter values are erroneous.

        :param weight: float, cat's weight (kg). Must be greater than zero.
        :param mood: str, describes cat's mood. Must have at least three
        characters.
        :raises: ValueError, if weight is less than or equal to zero or
        if mood is described with less than three letters.
        """
        # Try to set values for the attributes. Setters are called to avoid
        # the replication of the validity checks. The setters throw an exeption,
        # if they enconter an erroneus values. The exception is automatically
        # passed from this constructor to the caller.
        self.set_weight(weight)
        self.set_mood(mood)

    def get_weight(self):
        """Return cat's weight.

        :return: float, cat's weight in kilograms.
        """
        return self.__weight

    def set_weight(self, weight):
        """Try to change cat's weight. Raise an exception, if the parameter
        value is erroneous.

        :param weight: float, cat's weight (kg). Must be greater than zero.
        :raises: ValueError, if weight is less than or equal to zero.
        """
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError(f"Setting of weight failed: {weight} kg.")

    def get_mood(self):
        """Return cat's mood.

        :return: str, description of cat's mood.
        """
        return self.__mood

    def set_mood(self, mood):
        """Try to change cat's mood. Raise an exception, if the parameter
        value is erroneous.

        :param mood: str, describes cat's mood. Must have at least three characters.
        :raises: ValueError, if mood is decribed with less than three letters.
        """
        if len(mood) >= 3:
            self.__mood = mood
        else:
            raise ValueError(f"Setting of mood failed: \"{mood}\".")

    def printout(self):
        """Print the state of the cat object, that is, attribute values of
        the object to the screen."""
        print(f"weight: {self.__weight:.2f} kg")
        print(f"mood: \"{self.__mood}\"")

    def eat(self):
        """Nibble food so that cat's weight increases with five grams. Eating
        makes the cat happy.
        """
        self.__weight = self.__weight + 0.005
        # Food is happiness.
        print("Nom!")
        self.set_mood("happy")

    def greet(self, another):
        """Greet another object. Other cats deserve a special greeting. Cat does
        not greet itself.

        :param another: any type, the object to greet.
        """
        # To greet a cat, we need to know that the class of another object is Cat
        # and that another object is not the cat itself.
        if type(another) == Cat:
            # The another object must be someone else, because its reference
            # is not connected to this object.
            if self is not another:
                print("Meow!")
        # Not a cat.
        else:
            print("Meow.")

def create_a_cat_from_inputs():
    """Create a cat object and returns it. The object is initialized with
    the inputs from the user. The inputs are read from the user, until they
    are valid.

    :return: Cat, a reference to a newly created cat object.
    """
    # We do not have a cat yet.
    new_cat = None

    # The loop reiterates, if an exception is raised either from the built-in
    # type conversion function or from the constructor of the Cat class.
    valid_values = False
    while not valid_values:
        try:
            # Read cat's weight from the user as a string and try to convert
            # the string to a float. A ValueError is raised if the type
            # conversion fails.
            weight_str = input("Please, enter cat's weight in kilograms: ")
            weight = float(weight_str)
            # Read cat's mood from the user.
            mood_str = input("Please, descibe cat's mood: ")
            # Try to create a new cat. A ValueError is raised if the parameter
            # values are erroneous.
            new_cat = Cat(weight, mood_str)
            # The flag can be flipped, if no exceptions were raised.
            valid_values = True
        except ValueError:
            print("Invalid value!")

    # Return a reference to the newly created cat.
    return new_cat

def feed_the_cat(cat):
    """
    Feed the cat a small, random amount of its favourite food.

    :param cat: Cat, a hungry cat.
    """
    # It is assumed that from 1 to 30 titbits of food is available.
    titbits = randint(1, 30)

    # Feed the cat.
    while titbits > 0:
        cat.eat()
        titbits = titbits - 1

def main():
    # Create a new cat object in a function. A local reference need to be
    # attached the object to have it in the main function.
    mittens = create_a_cat_from_inputs()
    mittens.printout()

    # Changes made to the state of the mutable object in another function
    # are preserved after the function call. We see that the cat has had its
    # meal and is a happy camper, for a while.
    feed_the_cat(mittens)
    mittens.printout()

    # Attach another reference to the cat object. The cat has now two names:
    # "mittens" and "purrserk".
    purrserk = mittens
    print(mittens is purrserk) # True

    # The object can be accessed via either of the references.
    purrserk.set_mood("bonkers")
    print(mittens.get_mood()) # "bonkers"
    print(purrserk.get_mood()) # "bonkers"

    # The cat has no need to greet itself.
    mittens.greet(purrserk)

    # Greeting for another cat.
    whiskers = Cat(2.75, "curious") # "Meow!"
    mittens.greet(whiskers)

    # Greeting for a noncat.
    mittens.greet("(=^..^=)") # "Meow."

if __name__ == "__main__":
    main()
