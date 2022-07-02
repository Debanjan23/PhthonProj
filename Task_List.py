import collections
import logging

logging.basicConfig(filename="String_task.log", level=logging.DEBUG, format='%(asctime)s, %(levelname)s, %(message)s')
logging.info("this is my very first program with timestamp")


class ListTask(list):

    def __init__(self, *args):

        super(ListTask, self).__init__(args[0])

    def list_reverse(self):
        try:
            return self[::-1]

        except Exception as e:

            print(e)

    def fetch_item_count(self):
      try :
        a=input("Please provide me the no to fetch from list")

        return self.count(a)

      except Exception as e:
          print(e)



a= ListTask([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])

print(a.list_reverse())
print(a.fetch_item_count())