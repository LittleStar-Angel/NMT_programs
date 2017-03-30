import socket
import os
import sys
# Address
HOST = ''
PORT = 8000

text_content = '''
HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Update</p>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form> 
<form name="update" action="/" method="post">
<input type="submit" value="Update" name="update">
</form> 
</html>
'''

#f = open('test.jpg','rb')
#pic_content = pic_content + f.read()

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# Serve forever
while True:
    s.listen(3)
    conn, addr = s.accept()                    
    request    = conn.recv(1024)         # 1024 is the receiving buffer size
    method     = request.split(' ')[0]
    #src        = request.split(' ')[1]

    print 'Connected by', addr
    print 'Request is:', request

    # if GET method request
    if method == 'GET':
        content = text_content
        # send message
        conn.sendall(content)
    # if POST method request
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')             # Find the empty line
        entry = form[idx:]               # Main content of the request

        value = entry[-1].split('=')[-1]
        if value== 'Update':
		PID_ptzh = open("/home/luyi/pt-zh-worker-v1/PID").readline().rstrip()
		PID_zhpt = open("/home/luyi/zh-pt-worker-v1/PID").readline().rstrip()
		os.system('kill '+PID_ptzh)
		print ('kill pt-zh:'+PID_ptzh)
		os.system('bash /home/luyi/pt-zh-worker-v1/scripts/run_worker')		
		print ('Restart pt-zh')
		os.system('kill '+PID_zhpt)
		print ('kill zh-pt:'+PID_zhpt)
		os.system('bash /home/luyi/zh-pt-worker-v1/scripts/run_worker')		
		conn.sendall(text_content+'\n<p> Finished restart!</p>')
		print ('Restart zh-pt')
        # More operations, such as put the form into database
        # ...
        ######
    # close connection


    conn.close()
