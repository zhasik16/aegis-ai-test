def login_user():
    user_email = "test@example.com"
    # This should be flagged by Aegis AI
    print(user_email)
    
    user_data = {"name": "John Doe"}
    # This should also be flagged
    print(user_data)
    
    # This is fine - no user data
    print("Login successful")
    return True
