print(I demand your joy)
print(obviously for you not me)
while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("your feeling is incorrect,invalid and very inaccurate. Try again tomorrow.")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you better be. muack;)")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("ugh ikr. Let's go for eternal sleep together. I propose Hades. See Bob and ceberus yk. Ceberus likes rubber balls, you know. ")
      counter += 1

  if counter == 0:
    
      output = "I have a 3 word voababurary. Do guess and check."

  elif counter == 1:
    
      output = "It appears that you are feeling " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + " Hope you feel better :) "  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
