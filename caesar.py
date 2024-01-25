from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function
def caesar(start_text, shift_amount,cipher_direction, alphabet):
  end_text = ""
  for letter in start_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if cipher_direction == "decode":
        decrypted_position = position - shift_amount
        decrypted_letter = alphabet[decrypted_position]
        end_text += decrypted_letter
      elif cipher_direction == "encode":
        new_position = (position + shift_amount) % len(alphabet)
        new_letter = alphabet[new_position]
        end_text += new_letter
    else:
# If the character is not in the alphabet, add it to the end_text as is.
      end_text += letter

  print(f"The {cipher_direction}d text is: {end_text}")

#to continue the program based on user response
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to   decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction, alphabet=alphabet)
  result = input("Type 'yes' to go again. Otherwise type 'no.'\n")
  if result == "no":
    should_continue = False
    print("Bye!")