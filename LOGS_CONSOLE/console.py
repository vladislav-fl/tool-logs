from flask import Flask, request, Response, redirect, render_template

server: Flask = Flask()

@server.route('/')
def main():
    if request.method('GET'):
        return render_template('static/html/main.html')

@server.route('/test')
def test():
    if request.method('GET'):
        pass
    elif request.method('POST'):
        pass
    else:
        pass
