#code made by XYZ
def computepay(h,r):
    return 45.37
x=input("enter no. of hours:")
hrs=int(x)
y=input("enter no. of rate:")
rate=float(y)
if hrs<40:
    pay=hrs*rate
elif hrs>=40:
    pay=(40*rate)+(hrs-40)*rate*1.5

print("Pay",pay)
#heyy
