# SHA-1 Password Cracker

A Python implementation that attempts to crack SHA-1 hashed passwords using a dictionary attack against the top 10,000 most common passwords.

## Features

- **Dictionary Attack**: Uses a list of top 10,000 common passwords
- **Salt Support**: Optional salt functionality for more complex password schemes
- **Fast Lookup**: Efficient hash comparison using hashlib
- **Comprehensive Testing**: Unit tests included for validation

## Files

- `password_cracker.py` - Main implementation with the `crack_sha1_hash()` function
- `main.py` - Testing and demonstration script
- `test_module.py` - Unit tests for the password cracker
- `top-10000-passwords.txt` - Database of common passwords
- `known-salts.txt` - Salt strings for salted password cracking

## Usage

### Basic Usage

```python
from password_cracker import crack_sha1_hash

# Crack a password without salt
result = crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
print(result)  # Output: "password"
```

### With Salt Support

```python
# Crack a password with salt (salt + password + salt)
result = crack_sha1_hash("38e8a75f85b746778f11be8ba43c841e24a79341", use_salts=True)
print(result)  # Output: "superman"
```

## Function Signature

```python
def crack_sha1_hash(hash_to_crack, use_salts=False):
    """
    Takes in a SHA-1 hash of a password and returns the password if it is one 
    of the top 10,000 passwords used.
    
    Args:
        hash_to_crack (str): The SHA-1 hash to crack
        use_salts (bool): If True, prepend and append salt strings to passwords
    
    Returns:
        str: The cracked password or "PASSWORD NOT IN DATABASE"
    """
```

## Test Cases

### Without Salt
- `b305921a3723cd5d70a375cd21a61e60aabb84ec` → `"sammy123"`
- `c7ab388a5ebefb4d550652f1eb4d833e5316e3e` → `"abacab"`
- `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` → `"password"`

### With Salt (using salt "peppered")
- `38e8a75f85b746778f11be8ba43c841e24a79341` → `"superman"`
- `be2efdc8b319c980e1bb03ea48c5c949862c09bb` → `"q1w2e3r4t5"`
- `4355a5f6b8fd55bd8af019717a37498e25d07892` → `"bubbles1"`

## Running Tests

```bash
python main.py        # Run demonstration and tests
python test_module.py # Run unit tests only
```

## How It Works

1. **Load Password Database**: Reads passwords from `top-10000-passwords.txt`
2. **Salt Processing**: If `use_salts=True`, reads salt values from `known-salts.txt`
3. **Hash Generation**: For each password (with or without salt), generates SHA-1 hash
4. **Comparison**: Compares generated hash with target hash
5. **Return Result**: Returns the matching password or "PASSWORD NOT IN DATABASE"

### Salt Pattern

When `use_salts=True`, the function uses the pattern: `salt + password + salt`

## Deployment Ready

This implementation is ready for deployment on platforms like Railway. The code includes:
- Error handling for missing files
- Proper encoding (UTF-8)
- Comprehensive test coverage
- Clean, documented code structure

## Security Note

This tool is for educational and legitimate security testing purposes only. Always ensure you have proper authorization before attempting to crack passwords.

## Railway Deployment

This project is ready for deployment on Railway. The web server runs on the port specified by Railway's `PORT` environment variable.

### Files for Deployment
- `app.py` - Flask web server
- `requirements.txt` - Python dependencies  
- `Procfile` - Railway deployment configuration

### API Endpoints

- `GET /` - Web interface for testing
- `POST /crack` - Crack a password hash
- `GET /health` - Health check endpoint

### API Usage

```bash
curl -X POST https://your-app.railway.app/crack \
  -H "Content-Type: application/json" \
  -d '{"hash": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", "use_salts": false}'
```

Response:
```json
{
  "hash": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",
  "result": "password",
  "use_salts": false,
  "success": true
}
```

## Requirements

- Python 3.6+
- Flask 2.3.3
- gunicorn 21.2.0
- hashlib (built-in)
- unittest (built-in)