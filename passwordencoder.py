@author: Kennith Williams


# Initializing Variables
encoderRunning = True
newPassword = ""

#Password Encoder Function 
def encode(originalPassword):
    global newPassword
    #While original password isn't blank 
    while originalPassword != "":
      #intPassword = first character of the original password made into an integer
      intPassword = int(originalPassword[0:1])
      #Original password = everything after the first character
      originalPassword = originalPassword[1:]
      intPassword = (intPassword + 3) % 10
      #New password with the current digit concatinated onto it
      newPassword = newPassword + str(intPassword)

# Cade Challenger
# Password Decoder Function
def decode(encodedPassword):
    decodedPassword = ""
    for char in encodedPassword:
        intPassword = (int(char) - 3) % 10  # Shift back by 3
        decodedPassword += str(intPassword)
    return decodedPassword
# Cade Challenger

def main():
    global encoderRunning
    print("Menu \n -------------\n 1. Encode \n 2. Decode \n 3. Quit")
    optionSelect = int(input("Please enter an option:"))
    if optionSelect == 1:
        originalPassword = input("Please enter your password to encode:")
        #If the original password is comprised of 8 digits
        if originalPassword.isdigit and len(originalPassword) == 8:
          encode(originalPassword)
          print("Your password has been encoded and stored!")
        else: 
          print("Please enter an 8-digit numeric password.")

    # Cade Challenger
    elif optionSelect == 2:
        if newPassword:
            decodedPassword = decode(newPassword)
            print(f"The encoded password is {newPassword}, and the original password is {decodedPassword}.")
        else:
            print("No password has been encoded yet.")
    # Cade Challenger

    elif optionSelect == 3:
        #Setting encoderRunning to false ends the while loop
        encoderRunning = False
        
#This is set up to allow the user to quit  
while encoderRunning == True:
    main()
