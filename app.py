def login_user(email, password):
    # This is a potential PII leak!
    print(user_email)
    print("User logged in successfully")
    
def process_data(user_data):
    # This is fine
    print("Processing data")
    return user_data.upper()
