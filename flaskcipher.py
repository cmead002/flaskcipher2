from flask import Flask, render_template, request, url_for
import string

#Instantiate (create) our flask app object
app = Flask(__name__)
#debug mode so our browser doesn't cache (save) our page


#our index (main) page
@app.route('/')
def index():
    return render_template('index.html')

#encyption page
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    #if the user is requesting the page via GET request, just return our webpage in html
    if request.method == 'GET':
        return render_template('encrypt.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
    elif request.method == 'POST':
        message = (request.form["message"])
        key = int((request.form['key']))
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('encrypt.html', encrypted_message=encryptedmessage)

#decryption page
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    #if the user is requesting the page via GET request, just return our webpage in html
    if request.method == 'GET':
        return render_template('decrypt.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
    elif request.method == 'POST':
        message = (request.form["message"])
        key = int((request.form['key']))
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('decrypt.html', decrypted_message=encryptedmessage)


#function to encrypt users message using key provided
def encrypt_caesar(message, key):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)


#function to decrypt a message
def decrypt_caesar(message):
    def encrypt_caesar(message, key):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        table = str.maketrans(alphabet, shifted_alphabet)
        return message.translate(table)
app.run(debug=True)

# help from Zachary Forrest https://github.com/ZacharyForrest/caesar/blob/master/readme.md