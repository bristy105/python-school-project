"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 150164676
Name: Zannatul Ferdous
Email: zannatul.2.ferdous@tuni.fi

TODO
"""

# +--------------------------------------------------------------+
# | This template file requires at minimum Python version 3.8 to |
# | work correctly. If your Python version is older, you really  |
# | should get yourself a newer version.                         |
# +--------------------------------------------------------------+


LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        """ Creates a new object for the product
        param:   code, name, category, price, stock
        """

        # attributes:
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock
        self.__original_price = price

        # TODO (MAYBE): You might want to add more attributes here.

    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    def printout(self):
        # print the object

        print(self)

    def del_stock(self):

        """
        :param:no
        :return True/False
        """
        if self.__stock <= 0:
            self.__stock = 0
            return True
        else:
            return False

    def check_stock_low(self):
        """check the stock limit
        param: no
        return: true/false
        """
        if self.__stock < LOW_STOCK_LIMIT:
            return True
        else:
            return False

    # TODO: Multiple methods need to be written here to allow
    #       all the required commands to be implemented.
    def check_combine(self, other):

        """
        this function check the 'other' object can be combined or not on
        the basis of both object's price
        param: other(2nd object)

        """
        if self.__category == other.__category and self.__price == other.__price:

            self.__stock += other.__stock



        else:
            if self.__price != other.__price:
                print(f"Error: combining items with different prices {self.__price}€ and {other.__price}€.")

            if self.__category != other.__category:
                print(f"Error: combining items of different categories '{self.__category}' and '{other.__category}'.")

    def get_category(self):
        """
        param: none
        return: category

        """
        return self.__category

    def sale(self, amount):
        """calculate sale percentage
        param: amount"""
        self.__price = self.__original_price - (amount * 0.01) * self.__original_price


def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def printout(warehouse, parameters):
    """
    print all the object and print error also
    :param warehouse: dict[int, Product], dict of all known products.
       :param parameters: str, all the text that the user entered after the command word.
       """
    if parameters != "":
        if len(parameters) == 6:
            # print(type(parameters))
            parameters = int(parameters)
            # print(type(parameters))
            if type(int(parameters)) == int and int(parameters) in warehouse:
                for key in sorted(warehouse):
                    # print(key)
                    if key == parameters:
                        warehouse[parameters].printout()
            elif type(parameters) != int:
                print(f"Error: product '{parameters}' can not be printed as it does not exist.")
            elif int(parameters) not in warehouse:
                print(f"Error: product '{parameters}' can not be printed as it does not exist.")

        else:
            print(f"Error: product '{parameters}' can not be printed as it does not exist.")
    else:
        for parameters in sorted(warehouse):
            warehouse[parameters].printout()


def low(warehouse, parameters):
    """
    Prints all products in ascending order by product code whose
    inventory quantity has fallen below a preset limit.
     :param warehouse: dict[int, Product], dict of all known products.
       :param parameters: str, all the text that the user entered after the command word.
       """
    if parameters == '':
        for key in sorted(warehouse):
            if warehouse[key].check_stock_low():
                print(warehouse[key])


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = int(number)
        # print(code, number)
        for key in warehouse:

            # print(key)
            if key == int(code):
                # change
                warehouse[key].modify_stock_size(number)





    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    # print("Seems like everything is good.")
    # print(f"Parameters are: {code=} and {number=}.")


def change(warehouse, parameters):
    """
    Changes the inventory amount of the product indicated by the code by the amount
    accessing class's function.
    The amount can be a positive or negative integer:
     :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """
    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = int(number)
        # print(code, number)
        for key in warehouse:

            # print(key)
            if key == int(code):
                # change
                warehouse[key].modify_stock_size(number)
    except ValueError:
        print(f"Error: bad parameters '{parameters}' for change command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: stock for '{code}' can not be changed as it does not exist.")
        return


def delete(warehouse, parameters):
    """ this function deletes a product from the dict
     accessing object's function
    :param warehouse: dict[int, Product], dict of all known products.
       :param parameters: str, all the text that the user entered after the command word.
       """
    try:
        parameter = int(parameters)
        if parameter in warehouse:
            for key in sorted(warehouse):
                if key == parameter:
                    if warehouse[key].del_stock():
                        del warehouse[key]
                    else:
                        print(f"Error: product '{parameters}' can not be deleted as stock remains.")
        else:
            print(f"Error: product '{parameters}' can not be deleted as it does not exist.")






    except ValueError:
        print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
        return

        """ if (len(parameters) == 6):
        if  (type(parameters[-1]))==str:
            print( f"Error: product '{parameters}' can not be deleted as it does not exist.")

        else:
            if (type(int(parameters)) != int):
                print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
            elif (int(parameters) not in warehouse):
                print(f"Error: product '{parameters}' can not be deleted as it does not exist.")

            else:
                if (int(parameters) in warehouse):

                    if (warehouse[int(parameters)]).del_stock() == True:
                        del (warehouse[int(parameters)])


    else:
        print(f"Error: product '{parameters}' can not be deleted as it does not exist.")"""


def combine(warehouse, parameters):
    """
    combines 2 object's information accessing object's function into one
     and delete the second object
    from dictionary
    :param warehouse: dict[int, Product], dict of all known products.
       :param parameters: str, all the text that the user entered after the command word.
       """
    # print(parameters)
    try:
        former, later = parameters.split()
        former = int(former)
        later = int(later)
        # print(type(former),type(later))
        if former and later in warehouse:
            if former == later:
                print(f"Error: bad parameters '{parameters}' for combine command.")
            else:
                for key in sorted(warehouse):
                    if key == former:
                        (warehouse[key].check_combine(warehouse[later]))
                        del warehouse[later]

        else:
            print(f"Error: bad parameters '{parameters}' for combine command.")

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for combine command.")


def sale_percentage(warehouse, parameters):
    """
    calculate sale accessing object's function
    :param warehouse: dict[int, Product], dict of all known products.
           :param parameters: str, all the text that the user entered after the command word.
           """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        category, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        count = 0
        number = float(number)
        for key in sorted(warehouse):
            if category == warehouse[key].get_category():
                # print('category matches')
                count += 1
                (warehouse[key].sale(number))

        print(f'Sale price set for {count} items.')

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for sale command.")
        return


def main():
    filename = input("Enter database name: ")
    # filename = "products.txt"

    warehouse = read_database(filename)
    if warehouse is None:
        return
    flag = True
    while flag:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)

        command = command.lower()

        if len(parameters) == 0:
            parameters = ""
        else:
            parameters = parameters[0]
        # print(f"TEST: {command=} {parameters=}")

        # If you have trouble undestanding what the values
        # in the variables <command> and <parameters> are,
        # remove the '#' comment character from the next line.
        # print(f"TEST: {command=} {parameters=}")

        if "example".startswith(command) and parameters != "":
            """
            'Example' is not an actual command in the program. It is
            implemented only to allow you to get ideas how to handle
            the contents of the variable <parameters>.

            Example command expects user to enter two values after the
            command name: an integer and a float:

                Enter command: example 123456 1.23

            In this case the variable <parameters> would refer to
            the value "123456 1.23". In other words, everything that
                        was entered after the actual command name as a single string.
            """

            example_function_for_example_purposes(warehouse, parameters)

        elif "print".startswith(command) and parameters == "":
            printout(warehouse, parameters)

            # TODO: Implement print command which prints all
            #       known products in the ascending order of
            #       the product codes.

            ...



        elif "print".startswith(command) and parameters != "":
            # print(type((parameters)))
            printout(warehouse, parameters)
            # TODO: Implement print command to print a single
            #       product when the product code is given.
            ...

        elif "delete".startswith(command) and parameters != "":
            delete(warehouse, parameters)

            # TODO: Implement delete command for removing
            #       a product from the inventory.
            ...

        elif "change".startswith(command) and parameters != "":
            change(warehouse, parameters)
            # TODO: Implement change command which allows
            #       the user to modify the amount of a product
            #       in stock.
            ...

        elif "low".startswith(command) and parameters == "":
            low(warehouse, parameters)

            # TODO: Implement low command which can be used to
            #       alert the user when the amount of items
            #       drop below <LOW_STOCK_LIMIT> i.e. 30.
            ...

        elif "combine".startswith(command) and parameters != "":
            combine(warehouse, parameters)
            # TODO: Implement combine command which allows
            #       the combining of two products into one.
            ...

        elif "sale".startswith(command) and parameters != "":

            sale_percentage(warehouse, parameters)
            # TODO: Implement sale command which allows the user to set
            #       a sale price for all the products in a specific category.
            ...

        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
