#collect email from user
# split the email using the @, the first part as the username, the second part is gonna be saved as domain name
#split domain using .,

def main():
    print(" welcome to the email slicer")
    print("")


    email_input = input(" input your email address :  ")
    (username,domain)=email_input.split("@")
    (domain,extension) = domain.split(".")
    
    print("username :",username)
    print("Domain   :",domain)
    print("extensiona:",extension)
while True:
    main()