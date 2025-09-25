a="1234"
attempts = 3
while attempts >0:
    enter=input("enter the pin number:")
    if enter==a:
     print("pin accepted.access generated.")
     break
    else:
       attempts-=1
       if attempts > 0:
           print(f"invalid pin.{attempts} attempts(s) left.")
       else:
           print("card blocket. too many wrong attempts.")
    