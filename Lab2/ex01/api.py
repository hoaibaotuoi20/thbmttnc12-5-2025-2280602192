from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest  # Để xử lý lỗi đầu vào

# Assuming these cipher classes are in a 'cipher' directory/package
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Initialize cipher objects
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# Helper function for common error handling
def handle_error(e):
    """Handles errors and returns a JSON response."""
    if isinstance(e, BadRequest):
        return jsonify({'error': 'Invalid input: ' + e.description}), 400
    else:
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Register the error handler
app.register_error_handler(Exception, handle_error)

# CAESAR CIPHER ALGORITHM
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    """Encrypts plaintext using the Caesar cipher."""
    data = request.get_json()  # Use get_json() consistently
    if not data or 'plain_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'plain_text' or 'key' in request body")
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    """Decrypts ciphertext using the Caesar cipher."""
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'cipher_text' or 'key' in request body")
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# VIGENERE CIPHER ALGORITHM
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    """Encrypts plaintext using the Vigenere cipher."""
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'plain_text' or 'key' in request body")
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    """Decrypts ciphertext using the Vigenere cipher."""
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'cipher_text' or 'key' in request body")
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RAILFENCE CIPHER ALGORITHM
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_route():
    """Encrypts plaintext using the Rail Fence cipher."""
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'plain_text' or 'key' in request body")
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_route():
    """Decrypts ciphertext using the Rail Fence cipher."""
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'cipher_text' or 'key' in request body")
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'encrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    """Creates a Playfair matrix from a key."""
    data = request.get_json()
    if not data or 'key' not in data:
        raise BadRequest("Missing 'key' in request body")
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    """Encrypts plaintext using the Playfair cipher."""
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'plain_text' or 'key' in request body")
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    """Decrypts ciphertext using the Playfair cipher."""
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'cipher_text' or 'key' in request body")
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# TRANSPOSITION CIPHER ALGORITHM
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    """Encrypts plaintext using the transposition cipher."""
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'plain_text' or 'key' in request body")
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    """Decrypts ciphertext using the transposition cipher."""
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        raise BadRequest("Missing 'cipher_text' or 'key' in request body")
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
