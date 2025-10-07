def test_function():
    user_email = "test@example.com"
    print(user_email)  # This should be flagged
    print("Hello world")  # This should NOT be flagged
