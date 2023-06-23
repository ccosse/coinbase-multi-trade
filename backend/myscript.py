import socket, logging
FORMAT = '%(message)s'
logging.basicConfig(filename='/var/log/cbxd.log',level=logging.INFO, format=FORMAT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)

def log(msg):
  print(msg, end="\n")
  logging.info(msg)

def my_function_that_handles_data(d):
  log(d)

while True:
  conn, addr = s.accept()
  data = conn.recv(1024)
  conn.close()
  my_function_that_handles_data(data)