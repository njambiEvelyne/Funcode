import emoji
print("-"*40)
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if (marks >= 90):
  print(emoji.emojize(f"CONGRATULATIONs:sparkles: :cherry_blossom: {name.title()}. YOU SCORED A :sparkles: "))
  print(emoji.emojize("Graded successfully:check_mark_button:"))

elif (marks >= 80): 
  print(emoji.emojize(f"WELL DONE!:sparkles: :cherry_blossom: {name.title()}. YOU SCORED B :sparkles: "))
  print(emoji.emojize("Graded successfully:check_mark_button:"))

elif (marks >= 70): 
  print(emoji.emojize(f"WOW!:sparkles: :cherry_blossom: {name.title()}. YOU SCORED C :sparkles: "))
  print(emoji.emojize("Graded successfully:check_mark_button:"))

elif (marks >= 60): 
  print(emoji.emojize(f"GOOD TRIAL!:sparkles: :cherry_blossom: {name.title()}. YOU SCORED D. CAN DO BETTER :rose: "))
  print(emoji.emojize("Graded successfully:check_mark_button:"))

else:
  print(emoji.emojize(f"BELOW AVERAGE!:blue_heart: :cherry_blossom: {name.title()}. YOU SCORED F. CAN DO BETTER :rose: \n:warning: BE KEEN TO AVOID RETAKES :warning:"))
  print(emoji.emojize("Graded successfully:check_mark_button:"))
  


