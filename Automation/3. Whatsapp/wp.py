import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Test Message",14,41,15)
#pywhatkit.sendwhatmsg(phone_number, "Test")

# Send message to a group
#group_id = input("Enter group id: ")

#pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31)


