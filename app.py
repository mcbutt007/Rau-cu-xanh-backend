from flask import *
import sqlite3, base64, functools, shutil

# create the Flask app
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/main.db')
    conn.row_factory = sqlite3.Row
    return conn

# đường dẫn up hình, vd shop/<id>.png, user/234.png
@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory(r'database/images/',
                               filename, as_attachment=True)

# kiểm tra xem server có đang chạy hay không
@app.route('/', methods=['GET'])
def landing_page():
    return "Server is working!"

# trả về danh sách rau củ
@app.route('/home', methods=['POST','GET'])
def Home(one=False):
    conn = get_db_connection()
    feed = conn.execute('SELECT * FROM RAUCU')
    # convert query to json
    response = [dict((feed.description[i][0], value) \
        for i, value in enumerate(row)) for row in feed.fetchall()]
    conn.close()
    return jsonify((r[0] if response else None) if one else response)

# trả về thông tin rau củ theo id
@app.route('/raucuinfo/<id>', methods=['GET','POST'])
def RaucuInfo(id,one=False):
    conn = get_db_connection()
    raucuinfo = conn.execute('SELECT * FROM RAUCU WHERE RAUCU_ID = ?',
                            (id))
    response = [dict((raucuinfo.description[i][0], value) \
        for i, value in enumerate(row)) for row in raucuinfo.fetchall()]
    conn.close()
    # Output the query result as JSON
    return jsonify((r[0] if response else None) if one else response)

# trả về thông tin người dùng theo id
@app.route('/userinfo/<id>', methods=['GET','POST'])
def UserInfo(id,one=False):
    conn = get_db_connection()
    userinfo = conn.execute('SELECT * FROM USER WHERE USER_ID = ?',
                            (id))
    response = [dict((userinfo.description[i][0], value) \
        for i, value in enumerate(row)) for row in userinfo.fetchall()]
    conn.close()
    # Output the query result as JSON
    return jsonify((r[0] if response else None) if one else response)

# login trả về userid nếu thành công
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

# bỏ thông tin vào bảng RESET_PASSWORD_EMAIL, không làm gì khác.
@app.route('/resetpassword', methods=['POST'])
def recieve_email():
    # get email from POST request ex: /resetpassword?email=example%40gmail.com
    email = request.args.get('email')
    # Insert recieved email in to database

    conn = get_db_connection()
    conn.execute('INSERT INTO RESET_PASSWORD_EMAIL (EMAIL, TIME_STAMP) VALUES ( ?, CURRENT_TIMESTAMP )', (email,))
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
        # copy hình ảnh 0.png thành <USER_ID>.png trong /database/images/user
        # shutil.copy2('database/images/user/0.png', 'database/images/user/1.png')
        return "Đã tạo tài khoản thành công"
    else :
        return "Email tồn tại. Có phải bạn quên mật khẩu?"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.config['JSON_AS_ASCII'] = False # fix lỗi ko trả về dấu đươc
    app.run(debug=True, host='0.0.0.0', port=5000)
