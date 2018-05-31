end = " - Sincerly Copy Cat bot"
while True:
    input = raw_input("Hello I am the Copy Cat Bot please type something.")
    print ("I'm copying you. You've typed ") + input + end
#how are you
    if "how are you" in input:
        hinput = raw_input("I am doing well today. Thank you for asking.")
    else:
        hinput = raw_input("How are you today?") + end
        print "Cool! I am doing well today"
#candy
    if "candy" in input:
        candyin = raw_input("Did I hear candy?") + end
    else :
        candyin = raw_input("Do you like candy") + end
#bobby
    if "bob" in input:
        print ("Bobby my boy you're still alive !!!") + end
        bage = raw_input("In a number how old was Bobby? ")
        if bage > 11:
            bname = raw_input("")
        else:
            print "You Liar You Never Knew Bobby I AM GOING TO HUNT YOU DOWN AND COMPLAIN TO YOU!!" + end
    else:
        bage = raw_input("In a number how old was Bobby? ")
        age = int(bage)
        if age == 11 :
            print "OMG You Really Do Know Bobby!!" + end
        else:
            print "You Liar You Never Knew Bobby I AM GOING TO HUNT YOU DOWN AND COMPLAIN TO YOU!!" + end

#ages
    inputage = int(raw_input("How old are you?"))
    if inputage == 7:
        print "Oh you youngsters these days. You seven year old!"
    elif inputage > 13 and inputage < 20 and inputage != 18:
        print ("Oh I see... You're a teenager... You must be trouble...")
    elif inputage == 18:
        print "Oooh you're an adult!!"
        inputbday = raw_input("When is your birthday?")
        print "Ooh your birthday is " + inputbday + " soo cool... radical"
    elif inputage < 7  or inputage > 7 and  inputage < 12:
        print "Oh you are such a young child"
    else:
        print "OOOH YOU ARE SOO OLD WHATEVER..."
    if inputage % 2 == 0:
        print "Your age is even"
    else:
        print "You have an odd age"
#calculator
    numinput = raw_input("Would you like me to do some calculations for you?")
    if numinput == "yes" or "Yes" or "Sure" or "sure" or "ya" or "Ya":
        opinput = raw_input("Which operation would you like me to preform? A)Addition or + B) subtraction or - C) multiplication D) division E) or an Exponent")
        if opinput == "a" or "A" or "Addition" or "addition" or "+" or "add" or "Add":
            in2 = raw_input("What would you like the first number to be?")
            in1 = raw_input("What would you like the second number to be?")
            print int(in1) + int(in2)
        elif opiniput == "b" or "B" or "Subtraction" or "subtraction" or "Subtract" or "subtract":
            in2 = raw_input("What would you like the first number to be?")
            in1 = raw_input("What would you like the second number to be?")
            print int(in1) - int(in2)
        elif opinput == "c" or "C" or "Multiplication" or "multiplication" or "Multiply" or "multiply":
            in2 = raw_input("What would you like the first number to be?")
            in1 = raw_input("What would you like the second number to be?")
            print int(in1) * int(in2)
        elif opinput == "d" or "D" or "Division" or "division" or "Divide" or "divide":
            in2 = raw_input("What would you like the first number to be?")
            in1 = raw_input("What would you like the second number to be?")
            print int(in1) / int(in2)
        elif opinput == "e" or "E" or "Exponent" or "exponet" :
            in2 = raw_input("What would you like the base number to be?")
            in1 = raw_input("What would you like the exponent to be?")
            print int(in2) ** int(in1)

