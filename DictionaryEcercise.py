user_profile = {
        "username":'ravi',
        "age": 30,
        "weapons": ['gun', 'knife', 'shotgun', 'sniper'],
        "isactive": True,
        "clan": 'Indian Warrier'
        }

# print keys
for key in user_profile.keys():
    print(key)
    
# add new weapon
    
user_profile["weapons"].append('pan')

print(user_profile['weapons'])

# Add a new key to include 'is_banned'. Set it to false

user_profile['isbanned'] = False

print(user_profile)

#5 Ban the user by setting the previous key to True

user_profile['isbanned'] = True

print(user_profile)

#6 create a new user2 my copying the previous user and update the age value and username value.

new_user = user_profile.copy()
new_user['age']= 24
new_user['username'] ='manish'

print(new_user)