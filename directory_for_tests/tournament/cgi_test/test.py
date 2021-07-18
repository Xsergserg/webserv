#!/usr/bin/env python3
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("<h1>Hello world!</h1>")
print("<p>Your e-mail is ", form.getlist('email')[0], "</p>")

