def chatbot():
    # Welcome message
    print("Welcome to the chatbot!")

    # Collecting user's name and age
    name = input("What's your name? ")
    age = input("How old are you? ")

    # Greeting the user
    print(f"Hello, {name}! It's great to have someone who is {age} years old here.")

    # Ask how the chatbot can help
    print("\nHow can I assist you today?")

    # Displaying the menu options
    while True:
        print("\nMenu:")
        print("1. Option 1 (placeholder)")
        print("2. Option 2 (placeholder)")
        print("3. Option 3 (placeholder)")
        print("4. Exit")

        # Collect user's choice
        choice = input("Please choose an option (1-4): ")

        # Handling the user's choice
        if choice == "1":
            print("You selected Option 1 (placeholder).")
        elif choice == "2":
            print("You selected Option 2 (placeholder).")
        elif choice == "3":
            print("You selected Option 3 (placeholder).")
        elif choice == "4":
            print("Goodbye! Thanks for chatting!")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the chatbot function
chatbot()
