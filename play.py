import sys
from main import kahoot, error
import time

def get_input():
  try:
    name = sys.argv[1]
  except:
    name = input("name ")
  try:
    return str(name)
  except:
    print("Please input properly")
    error(0,"not proper input", True)

def esc():
  while send.end == False:
    if send.end == True:
      print("End!")
    else:
      time.sleep(0.1)

def testConnection(pin, name):
  send = kahoot(pin, name)
  return send.testSession2(pin)

def play(pin):
  if __name__ == '__main__':
    print("Initializing...")
    send = kahoot(pin, name)
    send.verify = True
    print("Connecting...")
    send.connect()
    print("Running Game...")
    send.run_game()
    esc()


name = get_input()

for num in range(100000,9999999):
  if testConnection(str(num), name):
    print(str(num))
  

