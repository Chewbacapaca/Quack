import random
import string

combo = string.ascii_letters + string.digits + string.punctuation

sample = random.choice(string.ascii_lowercase)      # At least one lowercase
sample += random.choice(string.ascii_uppercase)     # At least one uppercase
sample += random.choice(string.digits)     # At least one number
sample += random.choice(string.punctuation)    # At least one symbol
sample += ''.join(random.choice(combo) for i in range(4))  # Rest is a mix.
samplelist = list(sample)
random.shuffle(samplelist)

password = ''.join(samplelist)
print("Here's your random password: ")
print(password)
