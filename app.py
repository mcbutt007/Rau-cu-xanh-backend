from flask import Flask, json, jsonify, request, render_template
import sqlite3

# create the Flask app
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/main.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def check_login():
    #get username from POST request ex: /checklogin?username=Phuc&password=123456
    username = request.args.get('username')
    password = request.args.get('password')

    conn = get_db_connection()
    UsrID = conn.execute('SELECT USER_ID FROM USER WHERE USERNAME = ? AND PASSWORD = ?',
                        (username,password)).fetchone()
    conn.close()

    # return user id to the app
    if UsrID is None :
        return "0"
    return str(UsrID[0])

@app.route('/resetpassword', methods=['POST'])
def recieve_email():
    # get email from POST request ex: /resetpassword?email=example%40gmail.com
    email = request.args.get('email')
    # Insert recieved email in to database

    conn = get_db_connection()
    conn.execute('INSERT INTO FORGET_PASSWORD_EMAIL (EMAIL, TIME_STAMP) VALUES ( ?, CURRENT_TIMESTAMP )', (email,))
    conn.commit()
    conn.close()

    serverResponse = "Email đặt lại mật khẩu của bạn đã được ghi nhận"
    return serverResponse

@app.route('/registration', methods=['POST'])
def recieve_registration_info():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')

    # Check if email already in user database
    conn = get_db_connection()
    emailExists = conn.execute('SELECT USER_ID FROM USER WHERE EMAIL = ?', (email,)).fetchone()
    conn.close()

    # Neu khong co email trong db trung voi email dang ky
    if emailExists is None :
        # Insert recieved user info in to database
        conn = get_db_connection()
        conn.execute('INSERT INTO USER (USERNAME,EMAIL,PASSWORD,TIME_REGISTERED) VALUES (?, ?, ?,CURRENT_TIMESTAMP)', (username,email,password))
        conn.commit()
        conn.close()
        return "Đã tạo tài khoản thành công"
    else :
        return "Email tồn tại. Có phải bạn quên mật khẩu?"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
