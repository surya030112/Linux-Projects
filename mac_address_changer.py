import re
import subprocess
import psutil # not an inbuilt library

from random import choice, randint


addrs = psutil.net_if_addrs()
every_addr = addrs.keys()
list_addr = list(every_addr)


print("--------------------------------------------------------------------------------------------------------")

numb = []
for builtnum, inter in enumerate(list_addr):
    number = builtnum+1
    print(number, inter)
    numb.append(number)

num_interface = int(input("Enter the interface number you want to select: "))

interface = []

if(num_interface == numb[0]):
    interface = list_addr[0]
elif(num_interface == numb[1]):
    interface = list_addr[1]
elif (num_interface == numb[-1]):
    interface = list_addr[-1]
else:
    print("invalid option please enter the correct one")
print("The interface you have selected is :"+interface)

interface = str(interface)


def your_mac():
    string_mac = subprocess.check_output(["ifconfig "+str(interface)],shell =True)
    mac_search = str(re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(string_mac)))
    mac_addr = mac_search[41:-2]
    final_mac_addr = ("Your mac address(now) is "+mac_addr)
    print(final_mac_addr)
your_mac()
print("Please enter a valid option from the given below")
print("-----------------------------------------------------------------------")
print("1. Manual mac address \n2. Random mac address")
print("-----------------------------------------------------------------------")

inp = int(input())
def main():
    if inp == 1:

        change_mac()

    elif inp == 2:

        random_mac()

    else:
        print("please enter a valid option")



def change_mac():
    print( '''Please input the MAC Address in this format...\n---------------------------------------------------------------------------------------------------\nSpecified MAC Address : ff:ff:ff:ff:ff:ff''')
    manual_mac = input("Enter the custom MAC Address that you want to change to: ")
    subprocess.check_output(["ifconfig "+str(interface)+" down"],shell =True)
    subprocess.check_output(["ifconfig "+str(interface)+" hw ether "+ str(manual_mac)], shell = True)
    subprocess.check_output(["ifconfig "+str(interface)+" up"], shell = True)
    stringed_mac = subprocess.check_output(["ifconfig "+str(interface)],shell =True)
    mac_search_changed = str(re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(stringed_mac)))
    mac_addr_changed = mac_search_changed[-19:-2]
    final_mac_addr_changed = ("Your mac address(changed) is "+mac_addr_changed)
    print(final_mac_addr_changed)

def random_mac():
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)

    cisco = ["00","40","96"]
    dell = ["00","14","22"]

    mac_address_ra = choice([cisco, dell])

    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address_ra.append(three)


    mac_address_rand = (":".join(mac_address_ra))
    subprocess.check_output(["ifconfig "+str(interface)+" hw ether "+ str(mac_address_rand)], shell = True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell =True)
    stringed_mac_rand = subprocess.check_output(["ifconfig " + str(interface)], shell=True)
    mac_search_changed_rand= str(re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(stringed_mac_rand)))
    mac_addr_changed_rand= mac_search_changed_rand[-19:-2]
    final_mac_addr_rand = ("Your mac address(changed.random) is " + mac_addr_changed_rand)
    print(final_mac_addr_rand)

if __name__ == "__main__":
    main()

