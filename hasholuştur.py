import hashlib
from termcolor import colored

karakterGirin = input("Bir Kelime Girin: ")
print(colored("        >>>>>>>>>>>>Md5>>>>>>>>>>>> ","blue"))

hashjob = hashlib.md5()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green"))

print(colored("        >>>>>>>>>>>>Sha1>>>>>>>>>>>> ","blue"))

hashjob = hashlib.sha1()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green"))

print(colored("        >>>>>>>>>>>>Sha256>>>>>>>>>>>> ","blue"))

hashjob = hashlib.sha256()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green"))

print(colored("        >>>>>>>>>>>>512>>>>>>>>>>>>>","blue"))

hashjob = hashlib.sha512()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green"))
