from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'do not share your sercret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mysql'

mysql = MySQL(app)

# Route for handling the login page logic
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)

# Route for handling the logout page logic
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# Route for handling the registeration page logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'confirm_password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        full_name = request.form['fullName']
        phone = request.form['phone']
        country = request.form['country']
        gender = request.form['gender']
        birthday = request.form['birthday']
        join_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif password != confirm_password:
            msg = 'Password and Confirm Password do not match!'
        elif not username or not password or not confirm_password or not email or not full_name or not phone or not country or not gender or not birthday:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                           (username, password, confirm_password, email, full_name, phone, country, gender, birthday, join_date,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

# Route for handling the dashboard page logic
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))


#this is the route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Save the message to the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO messages (name, email, phone, message) VALUES (%s, %s, %s, %s)', (name, email, phone, message))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('thank_you'))

    return render_template('contact.html')
# Route for handling the thank you page logic
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')


#
@app.route('/updateAccount', methods=['GET', 'POST'])
def updateAccount():
    if request.method == 'GET':
        # Fetch user information from the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM accounts WHERE username = %s", (session['username'],))
        user_info = cursor.fetchone()
        cursor.close()
        return render_template('updateAccount.html', user_info=user_info)
    elif request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        full_name = request.form['full_name']
        phone = request.form['phone']
        country = request.form['country']
        gender = request.form['gender']
        birthday = request.form['birthday']

        # Update user information in the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("""
            UPDATE accounts
            SET email = %s, full_name = %s, phone = %s, country = %s, gender = %s, birthday = %s
            WHERE username = %s
        """, (email, full_name, phone, country, gender, birthday, session['username']))
        mysql.connection.commit()
        cursor.close()

        # Redirect the user to the account page
        return redirect(url_for('dashboard'))






# @app.route('/groups')
# def groups():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM `groups`")
#     groups = cur.fetchall()
#     cur.close()
#     return render_template('groups.html', groups=groups)

# # Route for creating a group
# @app.route('/create_group', methods=['GET', 'POST'])
# def create_group():
#     if request.method == 'POST':
#         group_name = request.form['group_name']
#         # Insert the group into the database
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO `groups` (group_name) VALUES (%s)", (group_name,))
#         mysql.connection.commit()
#         cur.close()
#         flash('Group created successfully', 'success')  # Flash message for success
#         return redirect(url_for('groups'))
#     return render_template('create_group.html')


# # Route for adding user to a group
# @app.route('/add_user_to_group/<int:group_id>', methods=['GET', 'POST'])
# def add_user_to_group(group_id):
#     if request.method == 'POST':
#         username = request.form['username']
#         permissions = request.form['permissions']
#         # Insert the user into the group in the database
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO group_members (group_id, username, permissions) VALUES (%s, %s, %s)", (group_id, username, permissions))
#         mysql.connection.commit()
#         cur.close()
#         return redirect(url_for('group_members', group_id=group_id))
#     return render_template('add_user_to_group.html', group_id=group_id)

# # Route for displaying group members
# @app.route('/group_members/<int:group_id>')
# def group_members(group_id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM group_members WHERE group_id = %s", (group_id,))
#     group_members = cur.fetchall()
#     cur.close()
#     return render_template('group_members.html', group_id=group_id, group_members=group_members)





@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/About')
def about():
    full_name = session.get('full_name') if 'loggedin' in session else None
    return render_template('About_Us.html', full_name=full_name)


if __name__ == "__main__":
    app.run(debug=True)
