from re import I


class Email:
    has_been_read = "Meassage read: "
    email_content = "Subject: "
    is_spam = "Spam: "
    from_address = "Sent by: "

    def __init__(self, address, is_spam, has_been_read):
        self.address = address
        self.is_spam = False
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

inbox = [Email]

def add_mail():
    mail = inbox
    print(mail)

add_mail()

def get_count():
    mail_count = len(inbox)
    print(mail_count)

get_count()

def get_emails():
    get_mail = int(input("What number is the email you want to get/read: "))
    mail = inbox[get_mail]
    print(mail)
    true_mail = Email
    true_mail.mark_as_read

get_emails()
    
def get_unread_emails():
    unread = Email
    print(unread.mark_as_read)

get_unread_emails()

def get_spam_emails(self):
    spam = Email
    print(spam.mark_as_spam)

get_spam_emails()

def delete():
    remove = int(input("What number is the email you want to delete: "))
    delete = inbox[remove]
    print(delete)

delete()

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        read = Email("Meassage read: ")
        print(read.mark_as_read)
    elif user_choice == "mark spam":
        spam = Email("Spam: ")
        print(spam.mark_as_spam)
    elif user_choice == "send":
        send = Email("Sent by: ")
        print(send.from_address)
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")