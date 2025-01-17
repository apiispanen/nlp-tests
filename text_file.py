texts = [
    "Amazon is expanding its logistics network in Europe.",
    "The new iPhone model is expected to release next month.",
    "Tesla's new battery technology promises longer ranges.",
    "Microsoft announced a new AI research center in China.",
    "The government is considering new regulations for cryptocurrencies.",
    "Facebook is facing a lawsuit over data privacy concerns.",
    "Uber is launching a new service in New York City.",
    "The Supreme Court ruled on the controversial case today.",
    "Walmart's earnings report exceeded Wall Street expectations.",
    "NASA successfully landed a rover on Mars.",
    "The stock market saw significant gains in tech stocks today.",
    "Airbnb's IPO was one of the most successful in history.",
    "The education department announced new student loan forgiveness plans.",
    "A new COVID-19 variant has been detected in South Africa.",
    "Google introduced new privacy features in its latest update.",
    "Twitter permanently banned a high-profile user for violating terms.",
    "Sony's latest gaming console sold out within minutes of release.",
    "The city council passed new environmental regulations.",
    "IBM is partnering with universities to advance quantum computing.",
    "A major earthquake struck the coast of Japan this morning.",
    
    "Amazon is planning to open new warehouses in Asia.",
    "The latest Samsung Galaxy is expected to be released next quarter.",
    "Tesla unveiled a new electric truck with improved range.",
    "Microsoft is opening a new data center in Germany.",
    "New cryptocurrency laws are being discussed by the government.",
    "Facebook is dealing with a major data breach.",
    "Uber's new service in Los Angeles is gaining popularity.",
    "The Supreme Court has made a decision on the recent healthcare case.",
    "Walmart's quarterly profits beat expectations.",
    "NASA's new space telescope is now operational.",
    "Tech stocks led the market rally today.",
    "Airbnb's stock soared after its successful IPO.",
    "New policies on student loans have been announced by the education department.",
    "A new strain of COVID-19 has emerged in Brazil.",
    "Google's new update includes enhanced security features.",
    "Twitter suspended several accounts for policy violations.",
    "Sony's new PlayStation model is in high demand.",
    "New laws on renewable energy were passed by the city council.",
    "IBM announced a collaboration with leading universities on quantum research.",
    "A significant earthquake was reported off the coast of Chile.",
    
    "Amazon to build new distribution centers in the US.",
    "The new OnePlus phone is set to launch next week.",
    "Tesla's latest solar panels offer greater efficiency.",
    "Microsoft is investing in a new AI lab in India.",
    "The government is drafting new rules for digital currencies.",
    "Facebook is under investigation for antitrust issues.",
    "Uber's expansion into Europe includes several new services.",
    "The Supreme Court will hear arguments on the immigration case tomorrow.",
    "Walmart's sales figures surpassed Wall Street predictions.",
    "NASA is preparing for a new mission to the moon.",
    "Investors are optimistic about the tech sector's growth.",
    "Airbnb's market debut was highly successful.",
    "The education department is introducing new guidelines for remote learning.",
    "A COVID-19 variant is spreading rapidly in India.",
    "Google's update aims to improve user privacy.",
    "Twitter is cracking down on misinformation.",
    "Sony's latest TV model is getting rave reviews.",
    "The city council is considering new housing regulations.",
    "IBM's quantum computing initiative is gaining traction.",
    "A powerful earthquake hit the Pacific Ocean near Alaska.",
    
    "Amazon is enhancing its delivery services in North America.",
    "The new Google Pixel phone will be available next month.",
    "Tesla's new self-driving feature is getting positive feedback.",
    "Microsoft is launching a new cybersecurity center in Israel.",
    "Government officials are debating new cryptocurrency policies.",
    "Facebook is launching a new privacy initiative.",
    "Uber is expanding its services to include grocery delivery.",
    "The Supreme Court has ruled on the voting rights case.",
    "Walmart's latest earnings report shows strong growth.",
    "NASA's Mars rover has sent back new images.",
    "Tech companies led the market surge today.",
    "Airbnb's IPO has been one of the biggest in recent years.",
    "New regulations for student loans have been proposed.",
    "A new COVID-19 variant has been discovered in the UK.",
    "Google's latest update focuses on user data protection.",
    "Twitter has removed several high-profile accounts.",
    "Sony's new camera technology is revolutionizing photography.",
    "The city council has approved new traffic regulations.",
    "IBM is investing heavily in quantum technology.",
    "A major earthquake was felt in California this morning.",
    
    "Amazon's new drone delivery service is being tested.",
    "The new Huawei smartphone is launching next quarter.",
    "Tesla's electric bikes are becoming popular.",
    "Microsoft's new cloud service is being rolled out globally.",
    "The government is introducing new regulations for online banking.",
    "Facebook's new ad policy is causing controversy.",
    "Uber's partnership with local businesses is expanding.",
    "The Supreme Court's decision on the environmental case is pending.",
    "Walmart's new health clinics are expanding nationwide.",
    "NASA's new satellite has been successfully launched.",
    "The tech industry is driving today's market gains.",
    "Airbnb's revenue exceeded expectations last quarter.",
    "The education department is reviewing student loan forgiveness applications.",
    "A COVID-19 variant has been found in Australia.",
    "Google's new tools aim to enhance internet security.",
    "Twitter's latest update addresses fake news.",
    "Sony's new headphones are top-rated by users.",
    "New environmental policies have been passed by the city council.",
    "IBM's new research facility focuses on quantum computing.",
    "An earthquake off the coast of Mexico caused minor damage.",
    
    "Amazon is expanding its grocery delivery services.",
    "The new Motorola phone is expected to be released next month.",
    "Tesla's new energy storage solutions are gaining traction.",
    "Microsoft's AI initiatives are expanding in Europe.",
    "The government is proposing new laws for fintech companies.",
    "Facebook is introducing new features for content creators.",
    "Uber's ride-sharing services are now available in more cities.",
    "The Supreme Court has ruled on the labor rights case.",
    "Walmart's new technology investments are paying off.",
    "NASA's mission to Mars is making progress.",
    "Tech stocks are leading the market rally.",
    "Airbnb's latest financial report shows strong growth.",
    "The education department is implementing new student loan policies.",
    "A COVID-19 variant has been detected in the US.",
    "Google's update includes new privacy controls.",
    "Twitter has introduced new community guidelines.",
    "Sony's new smartphone is receiving positive reviews.",
    "The city council has introduced new safety regulations.",
    "IBM is partnering with tech companies on quantum projects.",
    "An earthquake in Italy caused significant damage.",
    
    "Amazon is investing in renewable energy projects.",
    "The new LG phone is set to launch soon.",
    "Tesla's solar roof tiles are becoming more popular.",
    "Microsoft's new AI tools are being integrated into Office 365.",
    "The government is considering new regulations for AI technologies.",
    "Facebook's new algorithm changes are sparking debate.",
    "Uber is testing autonomous vehicles in San Francisco.",
    "The Supreme Court's ruling on the healthcare case is awaited.",
    "Walmart's new online platform is attracting more customers.",
    "NASA's new mission will explore the outer solar system.",
    "Tech companies are seeing strong earnings this quarter.",
    "Airbnb's growth is outpacing expectations.",
    "The education department is overhauling student loan policies.",
    "A new COVID-19 variant is spreading in Europe.",
    "Google's new app focuses on digital wellbeing.",
    "Twitter is implementing stricter verification processes.",
    "Sony's new gaming console is a hit among users.",
    "The city council is addressing new public health concerns.",
    "IBM's latest quantum computer is breaking new ground.",
    "An earthquake near New Zealand triggered a tsunami warning.",
    
    "Amazon's Prime Day sales broke records this year.",
    "The new Nokia phone is expected to be a game-changer.",
    "Tesla's new battery factory is under construction.",
    "Microsoft is developing new AI-powered healthcare solutions.",
    "The government is working on new privacy laws.",
    "Facebook is enhancing its live streaming features.",
    "Uber's food delivery service is expanding rapidly.",
    "The Supreme Court's decision on the patent case is forthcoming.",
    "Walmart's new store format is attracting attention.",
    "NASA's rover discovered signs of water on Mars.",
    "Tech stocks are driving the market higher.",
    "Airbnb's latest user statistics are impressive.",
    "The education department is simplifying the loan application process.",
    "A COVID-19 variant has been found in Canada.",
    "Google's new cloud services are gaining traction.",
    "Twitter is updating its policies on hate speech.",
    "Sony's new smart TVs are receiving great reviews.",
    "The city council is implementing new waste management policies.",
    "IBM's quantum research is advancing quickly.",
    "An earthquake in Indonesia caused widespread damage.",
    
    "Amazon is launching a new subscription service.",
    "The new HTC phone is launching next week.",
    "Tesla's autonomous driving technology is making headlines.",
    "Microsoft's new AI assistant is being praised.",
    "The government is drafting new cybersecurity regulations.",
    "Facebook's new marketplace feature is expanding.",
    "Uber's bike-sharing service is now available in more cities.",
    "The Supreme Court's ruling on the privacy case is imminent.",
    "Walmart's new logistics strategy is improving efficiency.",
    "NASA's new probe is heading to the asteroid belt.",
    "Tech sector earnings are beating expectations.",
    "Airbnb's user base is growing rapidly.",
    "The education department is working on new loan repayment plans.",
    "A COVID-19 variant has been identified in Russia.",
    "Google's latest update includes new AI capabilities.",
    "Twitter is addressing issues with automated accounts.",
    "Sony's new sound system is getting positive feedback.",
    "The city council is focusing on new transportation initiatives.",
    "IBM's quantum computing program is expanding.",
    "A major earthquake struck the Philippines this evening.",
    
    "Amazon is improving its customer service with AI.",
    "The new Oppo phone is gaining popularity.",
    "Tesla's new model is the fastest electric car yet.",
    "Microsoft's AI chatbot is being used in customer service.",
    "The government is introducing new digital tax laws.",
    "Facebook's new gaming platform is attracting users.",
    "Uber's new luxury service is launching in major cities.",
    "The Supreme Court's decision on the climate case is expected.",
    "Walmart's new mobile app is improving user experience.",
    "NASA's new mission is exploring deep space.",
    "Tech companies are leading the market recovery.",
    "Airbnb's latest partnership is boosting bookings.",
    "The education department is launching new financial aid programs.",
    "A COVID-19 variant has been reported in Japan.",
    "Google's new hardware products are hitting the market.",
    "Twitter is enhancing its user interface.",
    "Sony's new virtual reality headset is a hit.",
    "The city council is proposing new business regulations.",
    "IBM's quantum computing research is making headlines.",
    "An earthquake near Taiwan caused significant disruptions."
]

labels = [
    "business",
    "business",
    "technology",
    "technology",
    "policy",
    "business",
    "business",
    "policy",
    "business",
    "science",
    "business",
    "business",
    "policy",
    "health",
    "technology",
    "business",
    "business",
    "policy",
    "technology",
    "news"
] * 10


# let's line up the text and labels
for i in range(0, len(texts)):
    print(f"{texts[i]} ({labels[i]})")