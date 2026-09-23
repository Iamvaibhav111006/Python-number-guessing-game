import random
secret_number = random.randint(1, 100)
attempts = 0
user_guess = 0
while user_guess != secret_number:
  user_guess = int(input("enter your number: "))
  attempts += 1

  if user_guess == secret_number:
    print(secret_number)
  elif user_guess < secret_number:
      print("your number is low")
  elif user_guess > secret_number:
    print("your number is high")
print("number of attempts:", attempts)
