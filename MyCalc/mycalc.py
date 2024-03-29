
class MyCalc:

    ans = 0

    def _is_float(self, val):

        try:

            val = float(val)

            return True

        except:

            return False

    def _is_int(self, val):

        try:

            val = int(val)

            return True

        except:

            return False

    def _as_number(self, val):

        if self._is_int(val):

            return int(val)

        elif self._is_float(val):

            return float(val)

        else:

            raise Exception("Not a number")

    def add(self, number1, number2):

        if number1 == "ans":

            return self.add(self.ans, number2)

        else:

            number1 = self._as_number(number1)

            number2 = self._as_number(number2)

            self.ans = number1 + number2

        return self.ans

    def sub(self, number1, number2):

        if number1 == "ans":

            return self.sub(self.ans, number2)

        else:

            number1 = self._as_number(number1)

            number2 = self._as_number(number2)

            self.ans = number1 - number2

        return self.ans

    def mult(self, number1, number2):

        if number1 == "ans":

            return self.mult(self.ans, number2)

        else:

            number1 = self._as_number(number1)

            number2 = self._as_number(number2)

            self.ans = number1 * number2

        return self.ans

    def div(self, number1, number2):

        if number1 == "ans":

            return self.div(self.ans, number2)

        else:

            number1 = self._as_number(number1)

            number2 = self._as_number(number2)

            if number2 == 0:

                print("Can't divide by zero, sorry")

            else:

                self.ans = number1 / number2

        return self.ans

    # ucid= am3355 : 5/10/2022 : I am trying to make a square root

    def sqrt(self,N):

        if self._as_number(N) < 0:

            print('Square root of negative number does not exist!')

            return

        else:

            sqrt = self._as_number(N)**0.5 #this code gives square root of the number

            print('Square root of number {}: {}'.format(N,sqrt))

            return sqrt

 # ucid= am3355 : 5/10/2022 : I am trying to make a square

    def square(self, n):

        if self._as_number(n) < 0:

            return

        else:

            return self._as_number(n) ** 2 #this code gives square of the number

    # ucid= am3355 : 5/10/2022 : I am trying to make a sample mean

    def smean(self, data):

        n = len(data)

        for i in range(n):

            data[i] = self._as_number(data[i]) #this code gives sample mean of the numbers

        smean = sum(data) / n

        return smean

    # ucid= am3355 : 5/10/2022 : I am trying to make a median

    def median(self, L):

        L.sort()

        lLen = len(L)

        half = int(lLen / 2) #this code gives median of the numbers

        if lLen % 2 != 0:

            median = L[half]

        else:

            left = self._as_number(L[half - 1])

            right = self._as_number(L[half])

            # median = L[half - 1] + L[half]

            median = left + right

            median = median / 2

        return median

    # ucid= am3355 : 5/10/2022 : I am trying to make codes for mode

    def mode(self,data):

        counts = {}

        for item in data:

            num = self._as_number(item)

            if num in counts:

                counts[num] += 1

            else:

                counts[num] = 1 # These codes helps to find out the mode

        return counts

    def svariance(self, data): # ucid= am3355 : 5/10/2022 : I am trying to make a sample variance

        n = len(data)

        for i in range(n):

            data[i] = self._as_number(data[i])

        mean = sum(data) / n

        deviations = [(self._as_number(x) - mean) ** 2 for x in data]

        svariance = sum(deviations) / n #this code gives us the sample variance of numbers.

        return svariance

    def sstd_dev(self, ls): # ucid= am3355 : 5/10/2022 : I am trying to make a standard deviation

        n = len(ls)

        for i in range(len(ls)):

            ls[i] = self._as_number(ls[i])

        mean = sum(ls) / n

        var = sum((x - mean) ** 2 for x in ls) / n

        sstd_dev = var ** 0.5 #this code gives us the standard deviation of numbers.

        return sstd_dev

if __name__ == '__main__':

    is_running = True

    iSTR = input("Are you ready?")

    calc = MyCalc()

    print(calc)

    if iSTR == "yes":

        while is_running:

            iSTR = input("What is your eq:")

            if iSTR == "quit" or iSTR == "q":

                is_running = False

            else:

                print("Your eq was " + str(iSTR))

                if "+" in iSTR:

                    numbers = iSTR.split("+")

                    r = calc.add(numbers[0].strip(), numbers[1].strip())

                    print("R is " + str(r))

                # must be done before - check to hanlde negative values

                elif "/" in iSTR:

                    numbers = iSTR.split("/")

                    r = calc.div(numbers[0].strip(), numbers[1].strip())

                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:

                    numbers = iSTR.split("*") if "*" in iSTR else iSTR.split("x")

                    r = calc.mult(numbers[0].strip(), numbers[1].strip())

                    print("R is " + str(r))

                # must be done last so negative numbers work

                elif "-" in iSTR:

                    numbers = iSTR.split("-")

                    r = calc.sub(numbers[0].strip(), numbers[1].strip())

                    print("R is " + str(r))

                elif "smean" in iSTR:

                    print("doing smean")

                    numbers = iSTR.split("smean")[1].strip("[").strip("]").split(",")

                    r = calc.smean(numbers)

                    print("R is " + str(r))

                elif "median" in iSTR:

                    print("doing median")

                    numbers = iSTR.split("median")[1].strip("[").strip("]").split(",") # assumes a comma list of values for median

                    r = calc.median(numbers)

                    print("R is " + str(r))

                elif "mode" in iSTR:

                    print("doing mode")

                    numbers = iSTR.split("mode")[1].strip("[").strip("]").split(",")

                    r = calc.mode(numbers)

                    print("R is " + str(r))

                elif "sstd_dev" in iSTR:

                    print("doing sstd_dev")

                    numbers = iSTR.split("sstd_dev")[1].strip("[").strip("]").split(",")

                    r = calc.sstd_dev(numbers)

                    print("R is " + str(r))

                elif "svariance" in iSTR:

                    print("doing svariance")

                    numbers = iSTR.split("svariance")[1].strip("[").strip("]").split(",")

                    r = calc.svariance(numbers)

                    print("R is " + str(r))

                elif "sqrt" in iSTR:

                    numbers = iSTR.split("sqrt")[1].strip("[").strip("]")

                    r = calc.sqrt(numbers)

                    print("R is " + str(r))

                elif "square" in iSTR:

                    numbers = iSTR.split("square")[1].strip("[").strip("]")

                    r = calc.square(numbers)

                    print("R is " + str(r))

                    # etc

    else:

        print("Good bye")


