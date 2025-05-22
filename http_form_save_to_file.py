

# import socket

# HOST = '127.0.0.1'
# PORT = 1515

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(1)

# print(f"[Server Running] Visit: http://{HOST}:{PORT}")


# while True:
#     client_conn, client_addr =server_socket.accept()
#     request = client_conn.recv(1024).decode()
#     print("[Request Received]:\n", request)
    
#     request_line=request.splitlines()[0]
#     print(f"[the first line from request page {request_line}]")
    
#     method,path,_=request_line.split()
#     name=age=email=""
#     if method =="POST":
#         body=request.split("\r\n\r\n",1)[1]
#         print("[POST Body]:", body)
        
        
#         fields=body.split("&")
#         for field in fields:
#             key,value=field.split("=")
#             value=value.replace("+","")
#             if key =="name":
#                 name=value
#             elif key=="age":
#                 age=value
#             elif key=="email":
#                 email=value
#         #keep data in a file Text
#         if name and age and email:
#             with open ("data.txt","a") as file:
#                 file.write(f"Name: {name} | Age: {age} | Email: {email}\n")
#                 print("[Saved to File]")
#         if name :
#             message=f"<h2>Thanks, {name}!</h2><p>Your data was saved.</p>"
#         else:
#             message =""
            
            
#         html=f"""
#         <html>
#         <head><title>Save Form Data</title></head>
#         <body>
#             <h1>Submit Your Info</h1>
#             <form method="POST" action="/">
#                 <input type="text" name="name" placeholder="Your Name"><br>
#                 <input type="text" name="age" placeholder="Your Age"><br>
#                 <input type="email" name="email" placeholder="Your Email"><br>
#                 <button type="submit">Send</button>
#             </form>
            
            
#             {message}
#         </body>
#         </html>
#         """
#     response = f"""\
# HTTP/1.1 200 OK
# Content-Type: text/html
# Content-Length: {len("html")}

# {html}
# """

#     client_conn.sendall(response.encode())
#     client_conn.close()



import socket

HOST = '127.0.0.1'
PORT = 1515

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server Running] Visit: http://{HOST}:{PORT}")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(1024).decode()
    print("[Request Received]:\n", request)

    request_line = request.splitlines()[0]
    print(f"[First Line] {request_line}")

    method, path, _ = request_line.split()
    name = age = email = ""

    if method == "POST":
        body = request.split("\r\n\r\n", 1)[1]
        print("[POST Body]:", body)

        fields = body.split("&")
        for field in fields:
            key, value = field.split("=")
            value = value.replace("+", " ")
            if key == "name":
                name = value
            elif key == "age":
                age = value
            elif key == "email":
                email = value

        if name and age and email:
            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"Name: {name} | Age: {age} | Email: {email}\n")
                print("[Saved to File]")

    if name:
        message = f"<h2>Thanks, {name}!</h2><p>Your data was saved.</p>"
    else:
        message = ""

    html = f"""
    <html>
        <head><title>Save Form Data</title></head>
        <body>
            <h1>Submit Your Info</h1>
            <form method="POST" action="/">
                <input type="text" name="name" placeholder="Your Name"><br>
                <input type="text" name="age" placeholder="Your Age"><br>
                <input type="email" name="email" placeholder="Your Email"><br>
                <button type="submit">Send</button>
            </form>
            {message}
        </body>
    </html>
    """

    response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}
"""
    client_conn.sendall(response.encode())
    client_conn.close()
