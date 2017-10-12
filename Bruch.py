class Bruch(object):
    def __init__(self,*args):
        """
        :param args: The param has to be *args since you don't know how many arguments Bruch will have.
        args either is:
            -just one Value which is the Zähler and the nenner is 1
            -Two values with Zähler and Nenner
            -Or a Bruch object
        """
        if(len(args) == 1):
            #If argument is type of Bruch
            if(isinstance(args[0],Bruch)):
                #Set self.zaehler to Zähler of the argument
                self.zaehler = args[0].zaehler
                #Set self.nenner to Nenner of the argument
                self.nenner = args[0].nenner
            else:
                #Set self.zahler to the argument
                self.zaehler = args[0]
                #Set self.nenner to 1 since only one value was given
                self.nenner = 1
        else:
            #If Zähler and Nenner of the argument are both negative the Bruch will be positive
            if args[0] < 0 and args[1] < 0:
                self.zaehler = -args[0]
                self.nenner = -args[1]
            else:
                #Set self.zaehler to first argument
                self.zaehler = args[0]
                #Set self.nenner to second arugment
                self.nenner = args[1]

        #If self.nenner is 0 raise ZeroDvisionError
        if(self.nenner == 0):
            raise ZeroDivisionError("Keine Division durch 0!")

        #If self.nenner is not type of int raise TypeError
        if(not isinstance(self.nenner,int)):
            raise TypeError("Nenner muss ganzzahlig sein!")

        #If self.zaehler is not type of int raise TypeError
        if(not isinstance(self.zaehler,int)):
            raise TypeError("Zähler muss ganzzahlig sein!")

    def __float__(self):
        """
        Called by float()
        :return: float value of self.zaehler divided by self.nenner
        """
        return float(self.zaehler / self.nenner)

    def __int__(self):
        """
        Called by int()
        :return: Return int value (rounded off) of self.zaehler divided by self.nenner
        """
        return int(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Called by complex()
        :return: complex value of self.zaehler divided by self.nenner
        """
        return complex(self.zaehler / self.nenner)

    def __eq__(self, other):
        """
        Called by ==
        :param other: Value to be compared with
        :return: True if the 2 Bruchs are equal
        """
        if float(self) == float(other):
            return True

    def __lt__(self, other):
        """
        Called by <
        :param other:
        :return: True if self is less than other
        """
        if float(self) < float(other):
            return True

    def __le__(self, other):
        """
        Called by <=
        :param other: Value to be compared with
        :return: True if self is less than other or equal to other
        """
        if float(self) <= float(other):
            return True

    def __gt__(self, other):
        """
        Called by >
        :param other: Value to be compared with
        :return: True if self is greater than other
        """
        if float(self) > float(other):
            return True

    def __ge__(self, other):
        """
        Called by >=
        :param other: Value to be compared with
        :return: True if self is greater than other or equal to other
        """
        if float(self) >= float(other):
            return True

    def __invert__(self):
        """
        Called by ~
        :return: Bruch with Nenner and Zähler switched
        """
        return Bruch(self.nenner,self.zaehler)

    def __str__(self):
        """
        Called by str(), also called when printing
        :return: The Bruch in Parenthesis and with a Slash inbetween self.nenner and self.nenner
        If self.nenner is 1 then it'll only put out self.zaehler
        """
        if(self.nenner == 1):
            return '(' + str(self.zaehler) + ')'
        else:
            return '(' + str(self.zaehler) + '/' + str(self.nenner) + ')'

    def __pow__(self, power):
        """
        Called by **
        :param power: The exponent of the Bruch
        :return: Bruch with self.zaehler and self.nenner to the power of the exponent
        """
        return Bruch(self.zaehler ** power,self.nenner ** power)

    def __abs__(self):
        """
        Called by abs()
        :return: Bruch with the absolute values of self.zaehler and self.nenner
        """
        return Bruch(abs(self.zaehler),abs(self.nenner))

    def __neg__(self):
        """
        Called by -
        :return: Either Bruch with negative self.zaehler or Bruch with negative self.nenner => Double negative => Positive
        """
        if(self.zaehler < 0):
            return Bruch(-self.zaehler,self.nenner)
        elif(self.nenner < 0):
            return Bruch(self.zaehler,-self.nenner)


    @staticmethod
    def _Bruch__makeBruch(value):
        """
        The method has to be static because it creates a new Bruch based on only the parameter
        :param value: The Zähler of the Bruch to be created
        :return: Bruch based only on value
        """
        return Bruch(value,1)

    def __sub__(self, other):
        """
        Called by -
        :param other: The Object to be subtracted from self
        :return: Bruch with subtracted from other
        """
        #If other is an int you can just multiply self.nenner with other and subtract it from self.zaehler
        if (isinstance(other, int)):
            return Bruch(self.zaehler - (self.nenner * other), self.nenner)
        #if other is a Bruch you have to build the least common Multiple (Kleinstes Gemeinsames Vielfaches)
        #And calculate self.zaehler according to it
        elif (isinstance(other, Bruch)):
            zaehlerSelf = self.zaehler
            zaehlerOther = other.zaehler

            neuerNenner = lcm(self.nenner, other.nenner)
            zaehlerSelf *= neuerNenner / self.nenner
            zaehlerOther *= neuerNenner / other.nenner

            return Bruch(int(zaehlerSelf - zaehlerOther), neuerNenner)
        else:
            raise TypeError("Falsche Addition")

    def __isub__(self, other):
        """
        Called by -=
        :param other: The Object to be subtracted from self
        :return: Bruch with self subtracted from other
        """
        return self - other

    def __rsub__(self, other):
        """
        Called by -
        :param other: The object which gets self subtracted from it
        :return: Bruch with other subtracted from self
        """
        return Bruch(other) - self


    def __add__(self, other):
        """
        Called by +
        :param other: The Object to be added to self
        :return: Bruch with other added to self
        """
        # If other is an int you can just multiply self.nenner with other and add it to self.zaehler
        if(isinstance(other,int)):
            return Bruch(self.zaehler+(self.nenner*other),self.nenner)
        # if other is a Bruch you have to build the least common Multiple (Kleinstes Gemeinsames Vielfaches)
        # And calculate self.zaehler according to it
        elif(isinstance(other,Bruch)):
            zaehlerSelf = self.zaehler
            zaehlerOther = other.zaehler

            neuerNenner = lcm(self.nenner,other.nenner)
            zaehlerSelf *= neuerNenner / self.nenner
            zaehlerOther *= neuerNenner / other.nenner

            return Bruch(int(zaehlerSelf+zaehlerOther),neuerNenner)
        else:
            raise TypeError("Falsche Addition")

    def __iadd__(self, other):
        """
        Called by +=
        :param other: The Object to be added to self
        :return: Bruch with other added to self
        """
        return self + other

    def __radd__(self, other):
        """
        Called by +
        :param other: The Object which gets self added to it
        :return: Bruch with self added to other
        """
        return Bruch(other) + self

    def __truediv__(self, other):
        """
        Called by /
        :param other: The object which self gets divided by
        :return: Bruch with self divided by other
        """
        # If other is a Bruch you can just solve the double break ((Außen * Außen) / (Innen * Innen))
        if(isinstance(other,Bruch)):
            return Bruch(self.zaehler*other.nenner,self.nenner*other.zaehler)
        # If other is an int you can just make a Bruch out of other and call itself
        elif(isinstance(other,int)):
            return self / Bruch(other)
        # If other is 0 raise a ZeroDivisonError
        elif(other == 0):
            raise ZeroDivisionError
        else:
            raise TypeError("Falsche Division")

    def __itruediv__(self, other):
        """
        Called by /=
        :param other: The object which self gets divided by
        :return: Bruch with self divided by other
        """
        return self / other

    def __rtruediv__(self, other):
        """
        Called by /
        :param other: The object which gets divided by self
        :return: Bruch with other divided by self
        """
        return Bruch(other) / self

    def __iter__(self):
        """
        Called by z,n = Bruch(z,n)
        :return: Kind of a list which is iterable
        """
        #Iterate through self.zaehler and self.nenner
        for i in self.zaehler,self.nenner:
            #the keyword yield is basically the same as making a list, appending i each time and then returning this list
            yield i

    def __mul__(self, other):
        """
        Called by *
        :param other: The object which self gets multiplied by
        :return: Bruch with self mulitplied by other
        """
        # If other is a Bruch you can just solve the multiplication by mutliplying self.zaehler with other.zaehler and self.nenner with other.nenner
        if(isinstance(other,Bruch)):
            return Bruch(self.zaehler * other.zaehler, self.nenner*other.nenner)
        # If other is an int you can just make a Bruch out of other and call itself
        if(isinstance(other,int)):
            return self * Bruch(other)
        else:
            raise TypeError("Falsche Multiplikation")

    def __rmul__(self, other):
        """
        Called by *
        :param other: The object which gets multiplied by self
        :return: Bruch with other multiplied by self
        """
        return Bruch(other)*self

    def __imul__(self, other):
        """
        Called by *=
        :param other: The object which self gets multiplied by
        :return: Bruch with self mutliplied by other
        """
        return self * other



def lcm(x, y):
    """
    :param x: First integer
    :param y: Second integer
    :return: The least Common Multiple
    """
    # choose the greater number
    if x > y:
       greater = x
    else:
       greater = y

    # calculate the lcm
    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm