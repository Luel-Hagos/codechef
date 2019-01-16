withdraw,current_balance= input().split()
if int(withdraw)%5==0 and int(withdraw)<=(float(current_balance)-0.5):
    print("{:0.2f}".format(float(current_balance)-int(withdraw)-0.5))
else:
    print("{:0.2f}".format(float(current_balance)))