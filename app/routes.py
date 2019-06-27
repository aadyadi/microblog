from app import app

@app.route('/')
@app.route('/index')
def index():
    return """<html>
    <head><title> hey ya </title>
    <head>
    come here
    </html>"""
