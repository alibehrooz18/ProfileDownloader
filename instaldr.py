import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

L.interactive_login("fifa")

# Load a profile using its username
profile = instaloader.Profile.from_username(L.context, 'fifa')

# Fetch the followers of the profile
followers = [follower.username for follower in profile.get_followers()]

# Print the list of followers
print(followers)
print(profile.followees)
print(profile.get_profile_pic_url())


