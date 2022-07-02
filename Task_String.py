import logging

logging.basicConfig(filename="String_task.log", level=logging.DEBUG, format='%(asctime)s, %(levelname)s, %(message)s')
logging.info("this is my very first program with timestamp")


class StringTask:

    def __init__(self, s):
        try:
            self.jump = None
            self.upper_index = None
            self.lower_index = None
            self.s = s
        except Exception as e:

            print(e)

    def string_extraction(self, lower_index, upper_index, jump):
        try:
            self.lower_index = lower_index
            self.upper_index = upper_index
            self.jump = jump
            return self.s[self.lower_index:self.upper_index:self.jump]

        except Exception as e:
            print(e)

    def string_reverse(self):

        try:
            return self.s[::-1]

        except Exception as e:
            print(e)

    def string_uppercase_spilt(self):

        try:
            s2 = self.s.upper()
            return s2.split()

        except Exception as e:
            print(e)

    def string_lowercase(self):

        try:
            s2 = self.s.lower()
            return s2
        except Exception as e:
            print(e)

    def string_capitalize(self):

        try:
            s2 = self.s.capitalize()
            return s2

        except Exception as e:
            print(e)

    def string_strip(self):

        try:
            return self.s.strip()

        except Exception as e:
            print(e)

    def string_lstrip(self):

        try:
            return self.s.lstrip()

        except Exception as e:
            print(e)

    def string_rstrip(self):

        try:
            return self.s.lstrip()

        except Exception as e:
            print(e)

    def string_replacement(self):

        try:
            s2 = input("String please ")
            return self.s.replace(self.s, s2)

        except Exception as e:

            print(e)


s1 = StringTask("this is My First Python programming class and i am learNING python string and its function")
s3 = StringTask("Debanjan")
s4 = StringTask("     Debanjan    ")
print(s1.string_extraction(0, 500, 3))
print(s1.string_reverse())
print(s1.string_uppercase_spilt())
print(s1.string_capitalize())
print(s1.string_strip())
print(s1.string_lstrip())
print(s1.string_rstrip())
print(s3.string_replacement())
