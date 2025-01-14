# string length count
name = "vikky"
print(len(name))
print(name.endswith("ky"))
print(name.startswith("vi"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.replace("i","e"))

print(name.strip()) # to trim space
print(name.find("ky"))  # Returns 4
print(name.split())  # Returns ['vikky']
print(name.join(["Hi", " bro"]))  # Returns Hi vikky bro
print(name.isalpha())  # Returns True if all characters in the string are alphabetic.

print(name.isnumeric())  # Returns True if the string contains only numeric characters.
print(name.isalnum())  # Returns True if all characters in the string are alphanumeric.




