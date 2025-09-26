from flask import Flask, request, jsonify
from password_cracker import crack_sha1_hash
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>SHA-1 Password Cracker API</h1>
    <p>Use POST /crack to crack a SHA-1 hash</p>
    <h3>Example:</h3>
    <pre>
    POST /crack
    {
        "hash": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",  
        "use_salts": false
    }
    </pre>
    <h3>Test it:</h3>
    <form action="/crack" method="post">
        <label>Hash: <input type="text" name="hash" placeholder="SHA-1 hash" required></label><br><br>
        <label><input type="checkbox" name="use_salts" value="true"> Use salts</label><br><br>
        <button type="submit">Crack Password</button>
    </form>
    """

@app.route('/crack', methods=['POST'])
def crack_password():
    try:
        # Handle both JSON and form data
        if request.is_json:
            data = request.get_json()
            hash_to_crack = data.get('hash')
            use_salts = data.get('use_salts', False)
        else:
            hash_to_crack = request.form.get('hash')
            use_salts = request.form.get('use_salts') == 'true'
        
        if not hash_to_crack:
            return jsonify({'error': 'Hash parameter is required'}), 400
        
        # Validate hash format (SHA-1 should be 40 hex characters)
        if len(hash_to_crack) != 40 or not all(c in '0123456789abcdefABCDEF' for c in hash_to_crack):
            return jsonify({'error': 'Invalid SHA-1 hash format'}), 400
        
        result = crack_sha1_hash(hash_to_crack.lower(), use_salts)
        
        response = {
            'hash': hash_to_crack.lower(),
            'result': result,
            'use_salts': use_salts,
            'success': result != "PASSWORD NOT IN DATABASE"
        }
        
        if request.is_json:
            return jsonify(response)
        else:
            # Return HTML response for form submission
            status = "✅ Found" if response['success'] else "❌ Not found"
            return f"""
            <h2>Crack Result</h2>
            <p><strong>Hash:</strong> {hash_to_crack}</p>
            <p><strong>Use Salts:</strong> {use_salts}</p>
            <p><strong>Result:</strong> {result}</p>
            <p><strong>Status:</strong> {status}</p>
            <a href="/">← Back</a>
            """
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Railway provides PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)