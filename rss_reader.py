import feedparser

#feedUrl = "https://status.aws.amazon.com/rss/ec2-eu-west-1.rss"
feedUrl = input("Please enter the RSS feed url:")
d = feedparser.parse(feedUrl)
# Printing Channel information
print("--- Channel Information ---")
print(d['feed']['title'])
print(d['feed']['description'])
print(d['feed']['link'])
# print(len(d.entries))
print("--- Channel Information ---")

print("--- Item Information ---")

for i in range(len(d.entries)):
    print("Title: " + d.entries[i].title + ", Desc: " + d.entries[i].description + ", link:" + d.entries[i].link)

print("--- Item Information ---")