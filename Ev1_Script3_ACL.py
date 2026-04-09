acl_num = int(input("Cual es el numero IPv4 ACL? "))

if acl_num >= 1 and acl_num <=99:
    print("Este es un ACL IPv4 estándar. ")
elif acl_num >= 100 and acl_num <=199:
    print ("Este es un ACL IPv4 extendida. ")
else:
    print("Este ACL IPv4 no es extendida o estándar. ")