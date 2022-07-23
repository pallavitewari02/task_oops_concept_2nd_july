import logging
logging.basicConfig(filename="task1.log", level=logging.INFO)

class string :



    def __init__(self, s):
        self.s = s

    def slicing(self):
        logging.info("Here Slicing is performed:")
        try:
            q = self.s[1:301:3]
            return q
            logging.info("The outcome for slicing is %s",q)
        except Exception as e:
            logging.exception(e)

    def revers(self):
        logging.info("Here string reversal is performed:")

        try:
            q=self.s[::-1]
            return q
            logging.info("The outcome for reversal is %s",q)
        except Exception as e:
            logging.exception(e)

    def upr(self):
        logging.info("Here string is in upper case:")
        try:
            q=self.s.upper()
            return q
            logging.info("The outcome for string upper case is %s", q)
        except Exception as e:
            logging.exception(e)

    def split(self):
        logging.info("Splitting is performed:")
        try:
            q=self.s.split()
            return q
            logging.info("The outcome of the string splitting is %s", q)
        except Exception as e:
            logging.exception(e)

    def lowr(self):
         logging.info("Here String will be in Lower case:")
         try:
             q=self.s.lower()
             return q
             logging.info("The outcome of string in lower case is %s",q)
         except Exception as e:
            logging.exception(e)

    def capital(self):
         logging.info("Here the string will be in capital:")
         try:
             q = self.s.capitalize()
             return q
             logging.info("The outcome of string in capitalize is %s", q)
         except Exception as e:
            logging.exception(e)


strg=string("this is My First Python programming class and i am learNING python string and its function")

logging.info(strg.slicing())
logging.info(strg.revers())
logging.info(strg.upr())
logging.info(strg.split())
logging.info(strg.lowr())
logging.info(strg.capital())

# p=s[1:301:3]
# print(p)
# p=s[::-1]
# print(p)
# p=(s.upper())
# print(p.split())
# print(s.lower())
# print(s.capitalize())
# a="Pallavi Tewari"
# print(a.replace("i","o"))
# print(a.center(20,"*"))