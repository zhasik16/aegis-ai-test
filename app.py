import os

def login_user():
    # These will be flagged by Aegis AI
    user_email = "john@gmail.com"
    user_password = "secret123"
    api_key = "sk-123456789"
    
    print(user_email)  # 🚨 High risk!
    print(f"User logged in: {user_email}")  # 🚨 High risk!
    
    # This is better
    print("Login successful")
    
    return True

def process_payment():
    # More issues
    credit_card = "4111-1111-1111-1111"
    print(f"Processing: {credit_card}")  # 🚨 Critical!
    
    return "success"
