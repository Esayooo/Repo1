Information = ['name:Ersanat','gender: female','birthday:2001.06.06','nationality:Kazakh','major:computer science']
Specialties =['front-end website development','c++', 'python', 'c#']
Languages = ['Kazakh','Chinese','Russian']

Languages.append('English')
print(Languages)
print("------")
Information.extend(Specialties)
print(Information)
print("------")
Specialties.remove('c#')
print(Specialties)
print("------")
clear=Languages.clear()
print(clear)
print("------")

