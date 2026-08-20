class class_function_lib():
    def ai_subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def oddEven():
        num = int(input("Enter a number:"))
        if num%2==0:
            msg = " is even number"
        else:
            msg = " is odd number"
        print(num, msg)
    def check_eligibility():
        gender = input("Your Gender:")
        age =int(input("Your Age:"))
    
        if (gender == "Male" and age >= 21) or (gender == "Female" and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():    
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        
        tot = sub1+sub2+sub3+sub4+sub5
        per = tot/5
        print("Total : ", tot)
        print("Percentage : ", per)
    def triangle():
        hight = int(input("Height: "))
        breath = int(input("Breadth: "))
        tri = (hight*breath)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",tri)
              
        hgt1 = int(input("Height1: "))
        hgt2 = int(input("Height2: "))
        breath1 = int(input("Breadth: "))
        Perimtr = hgt1+hgt2+breath1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Perimtr)

    
    