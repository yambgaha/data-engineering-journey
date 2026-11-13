--data type: 
--int,float,complex, boolean, string, list, tuple, dictionary
 
--Casting 
a =1: b=float(a)
 
--String
single line a = "yam"/ a = 'yam'
multi line a = ''' yam....'''/ """yam......"""
string slicing print(a[0:5]) / a[-5:]
string modification : 
     upper(a), 
     lower(a), 
     replace("a", "b")-- replace all a with b
     split(",") -- split the string from "," symbol
string concatation
    a = "yam"; b ="gaha" print(a+ " " +b) -- " " is used for space or else the string will be joined.
Escape characters 
    \'	Single Quote -- used to get ' inside string
    \\	Backslash	
    \n	New Line	
    \t	Tab	
    \b	Backspace    
String methods
    capitalize()	Converts the first character to upper case
    find()	Searches the string for a specified value and returns the position of where it was found
F-Strings    
    To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)
 
Boolean
   In programming you often need to know if an expression is True or False.
   print(2>1) -- output is true
 
Python Operator
   Arithmetic Operators
        +, -, /, *, %, **  
        #division in python return float number
        ** is raise to 2**3 is 2^3
   Assignment Operator
        =	x = 5	x = 5	
        +=	x += 3	x = x + 3	
        -=	x -= 3	x = x - 3	
        *=	x *= 3	x = x * 3	
        /=	x /= 3	x = x / 3	
        %=	x %= 3	x = x % 3	
   Ternary Operator
        The ternary operator allows you to assign one value if a condition is true, and another if it is false:
        num = 6
        x = "WEEKEND!" if num > 5 else "Workday"
        print(x)
   comparison Operator
        ==	Equal	x == y	
        !=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
   logical operator
        and Returns True if both statements are true	
        or	Returns True if one of the statements is true	
        not	Reverse the result, returns False if the result is true	
   identity operator
        Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
        is 	Returns True if both variables are the same object	--x is y
        is not	Returns True if both variables are not the same object --x is not y
   bitwise operator
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
        |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
        ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
        ~	NOT	Inverts all the bits	~x
 
 
Lists are used to store multiple items in a single variable. Lists are created using square brackets:
    List items are ordered, changeable, and allow duplicate values.
    A list can contain different data types:
        eg list1 = ["apple", "orange", "apple",1,3,true]
        print(list1)
        len() -- to check length of list
        print(len(list))
    List items are indexed and you can access them by referring to the index number
        thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
        print(thislist[2:5])
    To change the value of a specific item, refer to the index number:
        thislist = ["apple", "banana", "cherry"]
        thislist[1] = "blackcurrant"
        print(thislist)
 
    insert():
        To insert a new list item, without replacing any of the existing values, we can use the insert() method.
        thislist = ["apple", "banana", "cherry"]
        thislist.insert(2, "watermelon")
        print(thislist)
    append()  
        To add an item to the end of the list
        thislist = ["apple", "banana", "cherry"]
        thislist.append("orange")
        print(thislist)
    extend()
        To append elements from another list to the current list
        thislist = ["apple", "banana", "cherry"]
        tropical = ["mango", "pineapple", "papaya"]
        thislist.extend(tropical)
        print(thislist)
    remove()
        this method removes the specified item. If there are more than one item with the specified value, the remove() method removes the first occurrence only not all.
        thislist = ["apple", "banana", "cherry", "banana"]
        thislist.remove("banana")
        print(thislist)
    pop()
        this method removes the specified index. If you do not specify the index, the pop() method removes the last item.
        thislist = ["apple", "banana", "cherry"]
        thislist.pop(1)
    del keyword can also delete the list completely.
        del list1
    clear()
         method empties the list.The list still remains, but it has no content.
         thislist = ["apple", "banana", "cherry"]
        thislist.clear()
    FOR Loop in list
        thislist = ["apple", "banana", "cherry"]
        for x in thislist:
        print(x)  --- print all elements of list
    While Loop
        thislist = ["apple", "banana", "cherry"]
        i = 0
        while i < len(thislist):
        print(thislist[i])
        i = i + 1
    newlist = [x for x in fruits] -- creating new list using loop can also use if in end for conditions.
    sort()
        method that will sort the list alphanumerically, ascending, by default:
        thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
        thislist.sort() --- user reverse = true for descending inside parenthesis
 
        You can also customize your own function by using the keyword argument key = function.
        def myfunc(n):
        return abs(n - 50)
        thislist = [100, 50, 65, 82, 23]
        thislist.sort(key = myfunc)
        print(thislist)
 
        By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
    copy()
        Copy 1 list to another
        list1 = [1,2,3,4]
        list2 = list1.copy()
        print(list2)    
 
Tuple: Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets. Tuple items are ordered, unchangeable, and allow duplicate values.
 
    tuple1 = ("red", "green", "blue")
    print(tuple1)
    print(tuple[0:2])
    print(len(tuple))
 
    Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple. after converting to list you can perform all list actions.   
        x = ("apple", "banana", "cherry")
        y = list(x)
        y[1] = "kiwi"
        x = tuple(y)
 
        print(x)
 
     
    del keyword can delete the tuple completely:
        thistuple = ("apple", "banana", "cherry")
        del thistuple
 
    Unpacking a Tuple
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple. But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
 
        fruits = ("apple", "banana", "cherry")
        (green, yellow, red) = fruits
        print(green)
        print(yellow)
        print(red)
 
 
        If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
 
            fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
            (green, yellow, *red) = fruits
            print(green)
            print(yellow)
            print(red) --- will print a list of 3 elements.
    Join Two Tuples: To join two or more tuples you can use the + operator:
        tuple1 = ("a", "b" , "c")
        tuple2 = (1, 2, 3)
        tuple3 = tuple1 + tuple2
        print(tuple3)
    Multiply Tuples: If you want to multiply the content of a tuple a given number of times, you can use the * operator:
        fruits = ("apple", "banana", "cherry")
        mytuple = fruits * 2
        print(mytuple)
 
Python Sets:Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed and no duplicate values if there are they will be considered as 1.
    thisset = {"apple", "banana", "cherry"}
    print(thisset)
 
    You cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
        thisset = {"apple", "banana", "cherry"}
        for x in thisset:
        print(x) -- print all values
 
 
        thisset = {"apple", "banana", "cherry"}
        print("banana" in thisset) -- output as true
 
    add(): Once a set is created, you cannot change its items, but you can add new items.
        thisset = {"apple", "banana", "cherry"}
        thisset.add("orange")
        print(thisset)
 
    update(): To add items from another set into the current set, use the update() method.
        thisset = {"apple", "banana", "cherry"}
        tropical = {"pineapple", "mango", "papaya"}
        thisset.update(tropical)
        print(thisset)
 
    remove()- to remove item
    discard()- to remove item
        thisset = {"apple", "banana", "cherry", mango}
        thisset.remove("banana") 
        thisset.remove("cherry")
        print(thisset)
 
    clear(): deletes only the elements of set
        thisset.clear()
    del: deletes the entire set
       del thisset
 
    Join SETS: There are several ways to join two or more sets in Python.
 
        The union() methods or use | to joins all items from both sets.
            set1 = {"a", "b", "c"}
            set2 = {1, 2, 3}
            set3 = set1.union(set2)
            OR
            set3 = set1 | set2
            print(set3)
 
        The intersection() method or & keeps ONLY the duplicates.
            set1 = {"apple", "banana", "cherry"}
            set2 = {"google", "microsoft", "apple"}
            set3 = set1 & set2
            print(set3)
 
        The difference() method or - keeps the items from the first set that are not in the other set(s).
            set1 = {"apple", "banana", "cherry"}
            set2 = {"google", "microsoft", "apple"}
            set3 = set1 - set2
            print(set3)
 
        The symmetric_difference() or ^ method keeps all items EXCEPT the duplicates.
            set1 = {"apple", "banana", "cherry"}
            set2 = {"google", "microsoft", "apple"}
            set3 = set1 ^ set2
            print(set3)
Python Dictionaries: Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:         
        thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        print(thisdict)    
    get(): to get values using keys
        x = thisdict.get("model")  -- using this will give value of model
    keys() method will return a list of all the keys in the dictionary.
        x = thisdict.keys()
    values() method will return a list of all the values in the dictionary
        x = thisdict.values()
    items() method will return each item in a dictionary, as tuples in a list.
        x = thisdict.items()
    Update() used to change existing values or create new ones
       thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        thisdict["year"] = 2018    --- normal way ony for existing key - values
        thisdict.update({"year" = 2018 })  -- using update to change or add new values
 
    Pop() method removes the item with the specified key name:
    Popitem() method removed the last iteam in python 3.7 onwards
        thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        thisdict.pop("model")   #removes the model key and valued
        thisdict.popitem()    #removed the last iteam of the dictionary
        print(thisdict)
    del: used to delete the entire dictonary
        del thisdict
    clear() removed all the key values of the dictionary
        thisdict.clear()
    dict/copy: used to copy a dictonary into a different var
        thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        dict1 = thisdict.copy()  #using copy
        dict2 = dict(thisdict)   #using dict
        print(mydict)
If statement : The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
    IF
        number = 15
        if number > 0:
            print("The number is positive")
 
    elif The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True
        a = 33
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
 
    Else: The else statement is executed when the if condition (and any elif conditions) evaluate to False.
        a = 200
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
        else:
            print("a is greater than b")
 
MATCH :match statement is used to perform different actions based on different conditions. IT can be used with set, dictonary list etc.
 
        day = 4
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
 
    Default Value: Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
        day = 4
        match day:
            case 6:
                print("Today is Saturday")
            case 7:
                print("Today is Sunday")
            case _:
                print("Looking forward to the Weekend")
    Combine Values:Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
        day = 4
        match day:
            case 1 | 2 | 3 | 4 | 5:
                print("Today is a weekday")
            case 6 | 7:
                print("I love weekends!")
 
LOOPS
    while loop: 
        i = 1
        while i < 6:
         print(i)
         i += 1
    for loop:
        for x in "banana":
         print(x)
 
Functions: A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoiding code repetition.
    def: used to create or define a function
        def my_function():   #creating a function
            print("Hello from a function")
        my_function()   # calling a function
 
    A parameter is the variable listed inside the parentheses in the function definition. An argument is the actual value that is sent to the function when it is called.
 
        def my_function(name): # name is a parameter
        print("Hello", name)
        my_function("Emil") # "Emil" is an argument
 
    Default parameter: You can assign default values to parameters. If the function is called without an argument, it uses the default value:
        def my_function(name = "friend"):
         print("Hello", name)
        my_function("Tobias")  gives hello tobias
        my_function()  # give hello friend 
    Keyword Arguments: You can send arguments with the key = value syntax.
        def my_function(animal, name):
         print("I have a", animal)
         print("My", animal + "'s name is", name)
 
        my_function(name = "Buddy", animal = "dog")
 
    Positional Arguments: When you call a function with arguments without using keywords, they are called positional arguments, they must be in the correct order:
        def my_function(animal, name):
            print("I have a", animal)
            print("My", animal + "'s name is", name)
 
        my_function("dog", "Buddy")
 
    Return Values: Functions can return values using the return statement:
        def my_function(x, y):
            return x + y
 
        print(result(1,2) )
 
    Positional-Only Arguments: To specify positional-only arguments, add , / after the arguments:
        def my_function(name, /):
            print("Hello", name)
        my_function("Emil")
 
    Keyword-Only Arguments: To specify that a function can have only keyword arguments, add *, before the arguments:
        def my_function(*, name):
            print("Hello", name)
 
        my_function(name = "Emil")
 
Python Decorators:Decorators let you add extra behavior to a function, without changing the function's code.
 
A decorator is a function that takes another function as input and returns a new function.
    def changecase(func):
    def myinner():
        return func().upper()
    return myinner
 
    @changecase
    def myfunction():
    return "Hello Sally"
 
    print(myfunction())
 
 
Recursion: Recursion is when a function calls itself.
    def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
 
    countdown(5)
 
Python RegEx:A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
 
    import re  # to downaload regex package
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
 
    []	A set of characters	"[a-m]"	
    \	Signals a special sequence (can also be used to escape special characters)	"\d"	
    .	Any character (except newline character)	"he..o"	
    ^	Starts with	"^hello"	
    $	Ends with	"planet$"	
    *	Zero or more occurrences	"he.*o"	
    +	One or more occurrences	"he.+o"	
    ?	Zero or one occurrences	"he.?o"	
    {}	Exactly the specified number of occurrences	"he.{2}o"	
    |	Either or	"falls|stays"	
    ()	Capture and group
 
Python Try Except:
    The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The else block lets you execute code when there is no error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks.
 
    Many Exceptions: You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
 
    else keyword to define a block of code to be executed if no errors were raised:
 
 
        try:
         print("Hello")
        except:
         print("Something went wrong")
        else:
         print("Nothing went wrong")
 
OOP stands for Object-Oriented Programming.
Classes: A class is a blueprint or template used to create objects.
Objects: An object is an instance of a class.
        class MyClass:
        x = 5
        p1 = MyClass()
        print(p1.x)
    del is used to delete object created
        del p1
 
    __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
        class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
 
        p1 = Person("Linus", 28)
 
        print(p1.name)
        print(p1.age)
    Encapsulation: Bundling data and methods, restricting direct access to some attributes.
    Inheritance: Reusing and extending existing classes.
    Polymorphism: Same interface, different implementations.
    Abstraction: Hiding internal details, exposing only necessary functionality.
 
    Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.
 
        class Person:
            def __init__(self, fname, lname):
                self.firstname = fname
                self.lastname = lname
 
            def printname(self):
                print(self.firstname, self.lastname)
 
        #Use the Person class to create an object, and then execute the printname method:
 
        x = Person("John", "Doe")
        x.printname()
 
 
        class Student(Person): # child class of Parent
            pass
 
    Polymorphism: The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
 
    Encapsulation: It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class. This prevents accidental changes to your data and hides the internal details of how your class works.
        Private Properties: In Python, you can make properties private by using a double underscore __ prefix.To access a private property, you can create a getter method:
 
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.__age = age
 
            def get_age(self):
                return self.__age
 
        p1 = Person("Tobias", 25)
        print(p1.get_age())
 
File Handling: Python has several functions for creating, reading, updating, and deleting files.
 
    The key function for working with files in Python is the open() function.
    The open() function takes two parameters; filename, and mode.
    There are four different methods (modes) for opening a file:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
    In addition you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)
    r+ for read and write
    w+ for write and read
    A+ for append and read
 
        f = open("demofile.txt", "rt")
 
    It is a good practice to always close the file when you are done with it.If you are not using the with statement, you must write a close statement in order to close the file:
        f.close()
 
    readline(): You can return one line by using the readline() method
        with open("demofile.txt") as f:
             print(f.readline())  #print first line
             print(f.readline())  #prints second line

    Python File Write:
 
        with open("demofile.txt", "a") as f:
            f.write("Now the file has more content!")
            f.seek(0) #brings cursor to index 0
            print(f.read()) #reads all data since fron curson
 
    Delete a File: To delete a file, you must import the OS module, and run its os.remove() function:
        import os
        os.remove("demofile.txt")
 
    Delete Folder:To delete an entire folder, use the os.rmdir() method:
        import os
        os.rmdir("myfolder")
 
CSV file:
    import csv
 
    with open("file.csv","r") as f:
    reader = csv.reader(f) 
    for row in reader:
    print(row)
 
    import csv
 
    with open("file.csv","r") as f:
        reader = csv.DictReader(f) # read as a dictionary
        for row in reader:
    print(row['id'],row['name'])
 
    create a new file and transfer data
        import csv
        with open("file.csv","r") as f:
            reader = csv.reader(f)
 
            with open("face.csv", "w") as fake:
                writer = csv.writer(fake,delimiter="-")
                for x in reader:
                    writer.writerow(x)
 
 
JSON file:
    import json
 
    with open("file.json","r") as f:
        data = json.load(f)
 
    print(data)
 
PANDAS: Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
 
        import pandas as pd
 
        mydataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
        }
 
        myvar = pd.DataFrame(mydataset)
 
        print(myvar)
 
    Pandas Series: A Pandas Series is like a column in a table.It is a one-dimensional array holding data of any type.
        import pandas as pd
        a = [1, 7, 2]
        myvar = pd.Series(a)
        print(myvar)
 
    Key/Value Objects as Series:
 
        import pandas as pd
        calories = {"day1": 420, "day2": 380, "day3": 390}
        myvar = pd.Series(calories)
        print(myvar)
 
    DataFrames:A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns. Series is like a column, a DataFrame is the whole table.
        import pandas as pd
 
        data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }
 
        #load data into a DataFrame object:
        df = pd.DataFrame(data)
 
        print(df) 
    Locate Row: loc attribute to return one or more specified rows but based on the row(indexed by default or indexed created by user) and column name
                iloc attribute to return one or more rows but based on row and column indexed by default
        print(df.loc[0,"name"]) # returns row 0 and column name
        print(df.iloc[0,0]) # return row 0 and column 0 no names can be used
 
        #to call multiple rows and columns
        print(df.loc[[1,2,3],["name","age"]])
        print(df.iloc[[1,2,3],[1,2]])
 
        #to call arange of rows and columns
        print(df.iloc[1:100, ;6]) # give first 100 rows with first 6 columns      
 
    Load Files Into a DataFrame: 
            import pandas as pd
 
            df = pd.read_csv('data.csv')
 
            print(df) 
    Named Indexes: With the index argument, you can name your own indexes.
        import pandas as pd
 
        data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }
 
        df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
 
        print(df)
 
 
    Read CSV
    use to_string() to print the entire DataFrame. If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
 
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.to_string())
 
    max_rows: The number of rows returned is defined in Pandas option settings. You can check your system's maximum rows with the pd.options.display.max_rows statement.
        import pandas as pd
 
        print(pd.options.display.max_rows) # print the no of rows it will display
 
        pd.options.display.max_rows = 9999 # changing the no of rows to be diplayed
 
        df = pd.read_csv('data.csv')
 
        print(df)
 
    head()/tail(): returns the headers/ footers and a specified number of rows, starting from the top.
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.head(10))  # displays the first 10 rows, if no number mention it will return top 5 rows
        print(df.tail(10))  # displays the last 10 rows, if no number mention it will return last 5 rows
 
    info(), that gives you more information about the data set.
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.info())
 
    Conditional statement in pandas:
    Filter rows
        df[df["age"] > 25]
 
    Multiple conditions
        df[(df["age"] > 25) & (df["salary"] > 50000)]  #AND Operator
        df[(df["age"] > 25) | (df["salary"] > 50000)]  #OR operator
        df1 = df[~(df["City"] == "Mumbai")]            #NOT operator
 
    Create a new column based on a condition
        df["status"] = "Junior"
        df.loc[df["age"] >= 30, "status"] = "Senior"    

 
 
    Cleaning DATA
    1. Empty cell:  Empty cells can potentially give you a wrong result when you analyze data.One way to deal with empty cells is to remove rows that contain empty cells.This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
 
    To add new column in data frame:
        df["New_column] = 1000  # will create new column and give value 1000 to all rows
        df["Salary_Hike"] = df["Salary"] + 100000 #will create new column name salary_hike
        print(df)
 
    add or make change in data
        df1 = df["Salary"] = df["Salary"] + 5000 #new datafram with only salary column
    rename() change column name
        df1 = df.rename(columns = {"Salary" : "Sal"})
 
    unique() gives unique value in the column
        df1 = df["City"].unique()
 
    value_counts() similar to groupby
        df1 = df["City"].value_counts()
    drop(): remove sepcified rows of columns:
        0 for row and 1 for column
        df.drop(1)  #drop row1
        df.drop(1,axis= 1)  #drop column 1
 
        df.drop(index = [1,2,3]) #drop rows
        df.drop(columns = [1,2,3])  #drop columns
 
        df.drop(index = df.index[1:5]) # drop a range of rows
 
        print(df.drop(index = df.index[1:5], columns = df.columns[1:3]))
        #drop a range of rows and columns

 
    dropna(): deletes rows which has null values you can create a new data frame or change the origional one
 
        #drop all rows with any column as null value
            df.dropna(how = "any",inplace = True)
 
        #drop all rows with all columns as null value
            df.dropna(how = "any",inplace = True)
        #droping rown only for specific columns
        df.dropna(subset=['Date'], inplace = True)
 
    fillna() method allows us to replace empty cells with a value:
 
        #replace value in sepcific column calories
            import pandas as pd
            df = pd.read_csv('data.csv')
            df.fillna({"calories": 130}, inplace=True)
        forward fill:
            df.fillna(method = "ffill")
 
        backword fill:
            df.fillna(method = "bfill")
 
    mean()/median()/mode() methods to calculate the respective values for a specified column:
 
        import pandas as pd
 
        df = pd.read_csv('data.csv')
 
        x = df["Calories"].mean()
        x = df["Calories"].median()
        x = df["Calories"].mode()[0]
 
        df.fillna({"Calories": x}, inplace=True)
 
        print(df.to_string())
 
    2. Data of Wrong Format: you have two options: remove the rows, or convert all cells in the columns into the same format.
        1.dropna(): 
        2. convert to correct format as per requirement
        eg for date use to_date, float(), int() as per requirement
    3. Wrong Data: "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99". 
        Replacing Values:
            df["Salary"].replace(1000, 2000, inplace=True)
 
    4.Removing Duplicates
        duplicated() method returns a Boolean values for each row:
            import pandas as pd
            df = pd.read_csv('data.csv')
            print(df.duplicated())
 
            #first duplicate is kept
            print(df.duplicated(keep="first"))
 
            #last duplicate is kep
            print(df.duplicated(keep="last"))
 
        drop_duplicates()
            import pandas as pd
            df = pd.read_csv('data.csv')
            df.drop_duplicates(inplace = True)
            print(df.to_string())
 
    Lamba function:
        df["New_Salary"] = df["Salary"].apply(lambda x: x+5000 if x > 6000 else x)
 
    concat: it can be used to join tables
 
    pd.concat(df1, df2)