#Creating a basic house value estimator
#Say Rs.10,000 is an additional value for each bedroom
#Every sq.ft is of value Rs.92
#Actual house value is Rs.450,000

def estimate_home_value(size_in_sqft,no_of_bedrooms):
    #Assume all homes are worth atleast Rs.50,000
    value=50000
    #Adjust the value estimate based on size of house
    value=value+(size_in_sqft*92)
    #Adjust the value estimate based on no. of bedrooms
    value=value+(no_of_bedrooms*10000)
    return value

area=int(input("Enter the total sqft of house "))
nob=int(input("Enter no. of bedrooms "))
value=estimate_home_value(area,nob)

print("Estimated Value of home:")
print(value)
