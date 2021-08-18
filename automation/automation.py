import re


with open('potential-contacts.txt',"r") as file:
    content=file.read()

    
phone_numbers=re.findall(r"\d{3}-\d{3}-\d{4}",content)

numbers=re.findall(r"\d{3}-\d{4}",content)
for number in numbers: 
    phone_numbers.append(f'206-{number}')

fixed_phone_number=[]
for number in phone_numbers:
    number=re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', number)
    fixed_phone_number.append(number)


test=[]  
with open('phone_numbers.txt','w+') as file:
    for number in fixed_phone_number:
        if number not in test:
            file.write(number + "\n")
            test.append(number)


#########################################################################################

emails=re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+",content)
test_emails=[]  
with open('emails.txt','w+') as file:
    for email in emails:
        if email not in test_emails:
            file.write(email + "\n")
            test_emails.append(email)



  
if __name__=="__main__":  
    print(fixed_phone_number)
    print(len(fixed_phone_number))
    print(len(emails))