# Extracted from https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
http://10.1.1.1:5000/login?username=alex&password=pw1

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    print(username)
    password = request.args.get('password')
    print(password)

