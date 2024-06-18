import time

def typing_master():
  text = "The quick brown fox jumps over the lazy dog."
  words = len(text.split())  # Count words by splitting the text
  start_time = time.time()
  user_input = input("Enter the number of words you want to type: ")
  user_words = int(user_input)

  print("Start typing the following text:")
  print(text)

  elapsed_time = time.time() - start_time
  typed_words = user_words - (words - len(input()))  # Calculate typed words

  print("\nTime:", elapsed_time, "seconds")
  print("Words typed:", typed_words)
  print("Speed:", typed_words / elapsed_time, "words per second")

typing_master()
