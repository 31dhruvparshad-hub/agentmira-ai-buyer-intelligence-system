from extractor import extract_buyer_profile

lead = """
"Hi there! So my husband Tom and I have been thinking about moving for a while now. 
We currently live in Chicago and the winters are just brutal, you know? My sister moved to Miami three years ago and she just loves it. We have two kids, Emma is 8 and Jack just turned 6, and our golden retriever Bella who is the sweetest. Tom works in finance and he can work remotely full-time, which is great. I'm thinking of starting a small consulting practice once we settle in. We've been talking about getting a house with a pool because the kids would absolutely love it, and Bella too honestly. Maybe 4 bedrooms because we want a guest room for when family visits. Tom really wants a dedicated home office. Budget-wise, we sold our place in Chicago and with our savings we could go up to about $1.4M, ideally $1.2M. Schools matter to us obviously. Coconut Grove or Coral Gables sounds nice from what we've researched? Looking forward to your suggestions!"""

profile = extract_buyer_profile(lead)

print(profile.nice_to_have_features)
print(profile.model_dump())