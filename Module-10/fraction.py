"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator


    def simplify(self):
        value = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator / value
        self.__denominator = self.__denominator / value
        return self.__str__()



    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        #print(self.__numerator,self.__denominator)
       # print((f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"))


        return (f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}")

    def complement(self):

        return Fraction(-self.__numerator,self.__denominator)

    #def reciprocal(self):
     #  return Fraction(self.__denominator,self.__numerator)

    def multiply(self,object_second):
        return Fraction(self.__numerator*object_second.__numerator,
                self.__denominator*object_second.__denominator)
    def divide(self,object_second):
        #print('self.__numerator: ',self.__numerator, 'second: ', object_second.__numerator)
        #print('self.__denominator: ',self.__denominator,'object_second.__denominator: ',object_second.__denominator)
        return Fraction(self.__numerator*object_second.__denominator,
                self.__denominator*object_second.__numerator)

    def add(self,object_second):
        return Fraction(self.__numerator * object_second.__denominator+
                        self.__denominator * object_second.__numerator,self.__denominator*object_second.__denominator)

    def deduct(self, object_second):
        return Fraction(self.__numerator * object_second.__denominator -
                        self.__denominator * object_second.__numerator,
                        self.__denominator * object_second.__denominator)
    def __lt__(self, object_second):
        l=self.__numerator/self.__denominator
        r=object_second.__numerator/object_second.__denominator
        return (l<r)
    def __gt__(self, object_second):
        l = self.__numerator / self.__denominator
        r = object_second.__numerator / object_second.__denominator
        return (l > r)


    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""
        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b
    return a

def main():
    ADD_COMMAND='add'
    PRINT_COMMAND='print'
    QUIT_COMMAND='quit'
    LIST_COMMAND='list'
    STAR_COMMAND='*'
    FILE_COMMAND='file'


    fraction_dict={}
    flag=True
    while flag:
        userCommand=input('> ')
        if userCommand==ADD_COMMAND:
            fracInput=input('Enter a fraction in the form integer/integer: ')
            key=input('Enter a name: ')
            string=fracInput.split('/')
            deno=int(string[1])
            numer=int(string[0])
            frac=Fraction(numer,deno)
            if key not in fraction_dict:
                fraction_dict[key]=frac
            #print(fraction_dict)

        elif userCommand ==PRINT_COMMAND:
            check=input('Enter a name: ')
            if check not in fraction_dict:
                print(f"Name {check} was not found")
            for key in fraction_dict:
                if check==key:
                    print(f'{key} = {fraction_dict[key]}')


        elif userCommand==QUIT_COMMAND:
            print('Bye bye!')
            flag=False
        elif userCommand==STAR_COMMAND:
            operand1=input('1st operand: ')
            operand2=input('2nd operand: ')
            if  operand1 not in fraction_dict:
                print(f'Name {operand1} was not found')
                return
            elif operand2 not in fraction_dict:
                print(f'Name {operand2} was not found')
                break
            print(f"{fraction_dict[operand1]} * {fraction_dict[operand2]} = {fraction_dict[operand1].multiply(fraction_dict[operand2])}")
            print('simplified', fraction_dict[operand1].multiply(fraction_dict[operand2]).simplify())

        elif userCommand==LIST_COMMAND:
            for key in sorted(fraction_dict):
                print(f"{key} = {fraction_dict[key]}")

        elif userCommand==FILE_COMMAND:
            fileName = input('Enter the name of the file: ')
            try:

                file= open(fileName,mode='r'
                                         )


            except OSError:
                print('Error: the file cannot be read.')
                return
            for key in file:
                line = key + ',' + fraction_dict[key]
                print(line)
            fraction_name = fields[0]
            nd = fields[1].split("/")
            numerator = nd[0]
            denominator = nd[1]
            fraction_dictionary[fraction_name] = Fraction(int(numerator), int(denominator))
        file.close()

        else:
            print('Unknown command!')




           #file.close()












if __name__ == '__main__':
    main()