# Sample training data with made-up articles and their headlines
articles = [
    "The stock market saw a significant increase today with major indices showing gains across the board. \
    Investors are optimistic about the upcoming earnings season, expecting strong performance from key sectors. \
    Analysts attribute the gains to positive economic data and improved investor sentiment. \
    The technology sector led the rally, with several major tech companies reporting better-than-expected earnings. \
    Experts caution, however, that market volatility may continue in the short term due to geopolitical uncertainties.",

    "In a historic move, the government has announced a new policy aimed at reducing carbon emissions by 50% over the next decade. \
    The policy includes measures such as increased investment in renewable energy, stricter regulations on industrial emissions, and incentives for green technologies. \
    Environmental groups have praised the policy, calling it a significant step towards combating climate change. \
    Critics, however, argue that the policy does not go far enough and lacks enforcement mechanisms. \
    The government has pledged to work with industry stakeholders to ensure successful implementation of the policy.",

    "A breakthrough in medical research has led to a new treatment for a rare disease, offering hope to millions. \
    The new treatment, developed by a team of international scientists, has shown promising results in early clinical trials. \
    Patients who received the treatment experienced significant improvements in their condition, with minimal side effects. \
    Researchers are optimistic that the treatment could be available to the public within the next few years. \
    The discovery has been hailed as a major milestone in the fight against rare diseases.",

    "Tech companies are racing to develop the next generation of artificial intelligence, promising unprecedented advancements. \
    Major players in the tech industry are investing heavily in AI research and development, aiming to create smarter and more efficient systems. \
    AI experts predict that the next wave of innovations will revolutionize industries such as healthcare, finance, and transportation. \
    However, there are concerns about the ethical implications of AI and its potential impact on jobs. \
    Industry leaders are calling for the establishment of guidelines to ensure the responsible development and deployment of AI technologies.",

    "The local community came together to celebrate the annual festival, showcasing cultural diversity and unity. \
    The festival featured a variety of activities, including music and dance performances, art exhibitions, and food stalls offering cuisines from around the world. \
    Attendees expressed their appreciation for the opportunity to learn about different cultures and traditions. \
    Organizers emphasized the importance of fostering a sense of community and inclusivity. \
    The event concluded with a grand fireworks display, leaving attendees eagerly anticipating next year's festival.",

    "The renewable energy sector is experiencing rapid growth, driven by technological advancements and supportive government policies. \
    Solar and wind power installations are increasing at an unprecedented rate, reducing dependence on fossil fuels. \
    Experts predict that renewable energy will soon become the dominant source of power in many regions. \
    This shift is expected to have significant environmental benefits, including reduced greenhouse gas emissions. \
    However, there are challenges to be addressed, such as energy storage and grid integration.",

    "Advancements in biotechnology are paving the way for new medical treatments and therapies. \
    Researchers are exploring the potential of gene editing, personalized medicine, and regenerative therapies. \
    These innovations promise to improve patient outcomes and reduce healthcare costs. \
    The biotech industry is attracting substantial investment, with numerous startups emerging in the field. \
    Despite the promise, there are ethical and regulatory challenges that need to be addressed.",

    "The transportation industry is undergoing a transformation with the development of autonomous vehicles. \
    Self-driving cars and trucks are expected to improve road safety and reduce traffic congestion. \
    Major automotive companies are investing in autonomous vehicle technology, conducting extensive testing and trials. \
    The adoption of autonomous vehicles raises questions about regulations and the future of employment in the sector. \
    Experts believe that the widespread use of autonomous vehicles is still several years away.",

    "The financial sector is embracing blockchain technology, which promises to revolutionize how transactions are conducted. \
    Blockchain provides a secure and transparent way to record transactions, reducing the risk of fraud. \
    Financial institutions are exploring the use of blockchain for various applications, including cross-border payments and smart contracts. \
    The technology is still in its early stages, and there are challenges to be addressed, such as scalability and regulatory compliance. \
    Despite these challenges, the potential benefits of blockchain are driving continued interest and investment.",

    "The education system is evolving with the integration of digital tools and technologies. \
    Online learning platforms and virtual classrooms are providing new opportunities for students and educators. \
    These tools offer flexibility and accessibility, enabling lifelong learning and professional development. \
    However, there are concerns about the digital divide and the need for effective teaching methods in a virtual environment. \
    Policymakers and educators are working together to ensure that the benefits of digital education are realized by all students.",

    "The healthcare industry is leveraging big data and analytics to improve patient care and outcomes. \
    Data from electronic health records, wearable devices, and other sources are being used to identify trends and inform clinical decisions. \
    Predictive analytics is helping to identify patients at risk of developing certain conditions, enabling early intervention. \
    The use of big data is also driving advances in personalized medicine, allowing treatments to be tailored to individual patients. \
    While the potential benefits are significant, there are concerns about data privacy and security.",

    "Climate change is becoming an increasingly urgent global issue, with scientists warning of its severe impacts. \
    Rising temperatures, extreme weather events, and sea level rise are among the major concerns. \
    Governments and organizations around the world are taking action to mitigate the effects of climate change. \
    This includes transitioning to renewable energy, implementing carbon pricing, and investing in climate resilience. \
    Despite these efforts, experts stress the need for more ambitious and coordinated action to address the crisis.",

    "The agricultural sector is adopting new technologies to increase productivity and sustainability. \
    Precision farming, drones, and IoT devices are being used to monitor crops and optimize resource use. \
    These technologies are helping farmers to improve yields, reduce costs, and minimize environmental impact. \
    The adoption of agtech is also supporting the development of sustainable farming practices. \
    However, there are challenges related to technology adoption and access for small-scale farmers.",

    "The retail industry is undergoing a transformation with the rise of e-commerce and digital technologies. \
    Online shopping platforms are offering consumers convenience and a wider range of products. \
    Retailers are using data analytics and AI to personalize the shopping experience and improve customer service. \
    The shift to digital is also leading to changes in supply chain management and logistics. \
    However, the growth of e-commerce presents challenges for traditional brick-and-mortar stores.",

    "The entertainment industry is evolving with the advent of streaming services and digital media. \
    Consumers are increasingly turning to online platforms for movies, music, and other forms of entertainment. \
    Streaming services are investing in original content to attract and retain subscribers. \
    The shift to digital is also impacting the traditional media landscape, leading to changes in advertising and distribution. \
    Despite the growth of streaming, there are challenges related to content piracy and intellectual property rights.",

    "The space industry is entering a new era of exploration and innovation. \
    Private companies are playing a significant role in space missions and research. \
    Advances in technology are enabling new capabilities, such as reusable rockets and satellite networks. \
    Governments and organizations are collaborating on ambitious projects, including missions to Mars and the Moon. \
    The growth of the space industry is driving investment and interest in STEM education and careers.",

    "The hospitality industry is adapting to changing consumer preferences and technological advancements. \
    Hotels and resorts are using digital tools to enhance the guest experience and streamline operations. \
    The rise of short-term rental platforms is also impacting the traditional hospitality sector. \
    Sustainability and eco-friendly practices are becoming increasingly important to travelers. \
    The industry is exploring new ways to meet the evolving needs of customers while maintaining profitability.",

    "The fashion industry is embracing sustainability and innovation. \
    Brands are adopting eco-friendly materials and ethical production practices. \
    Technology is playing a key role, with innovations such as 3D printing and virtual fashion. \
    Consumers are becoming more conscious of the environmental impact of their purchases. \
    The industry is also exploring new business models, such as rental and resale platforms.",

    "The energy sector is transitioning towards cleaner and more sustainable sources of power. \
    Investments in renewable energy, energy storage, and smart grids are increasing. \
    The shift is driven by the need to reduce greenhouse gas emissions and combat climate change. \
    Technological advancements are making renewable energy more affordable and efficient. \
    However, there are challenges related to infrastructure, policy, and market dynamics.",

    "The automotive industry is experiencing significant changes with the rise of electric vehicles (EVs). \
    Major automakers are investing in EV technology and expanding their electric vehicle offerings. \
    Government incentives and policies are supporting the adoption of EVs. \
    Advances in battery technology are improving the range and performance of electric vehicles. \
    The growth of the EV market is also driving the development of charging infrastructure and renewable energy integration.",

    "The food and beverage industry is evolving with changing consumer preferences and technological innovations. \
    Plant-based and alternative proteins are gaining popularity as consumers seek healthier and more sustainable options. \
    Technology is also playing a role in improving food safety and supply chain transparency. \
    The rise of food delivery platforms is changing how consumers access and enjoy meals. \
    Despite these trends, the industry faces challenges related to regulation, sustainability, and consumer trust.",

    "The travel industry is rebounding as restrictions ease and consumer confidence returns. \
    Airlines, hotels, and tour operators are seeing an increase in bookings and travel activity. \
    The industry is adopting new health and safety protocols to ensure the well-being of travelers. \
    Technology is playing a crucial role in facilitating travel, from contactless check-ins to digital health passports. \
    The future of travel is expected to be shaped by sustainability, innovation, and changing consumer preferences.",

    "The telecommunications industry is advancing with the rollout of 5G networks. \
    5G technology promises faster internet speeds, lower latency, and improved connectivity. \
    Telecom companies are investing heavily in infrastructure to support the deployment of 5G. \
    The new technology is expected to drive innovation in various sectors, including IoT, healthcare, and smart cities. \
    However, there are challenges related to spectrum allocation, security, and the digital divide.",

    "The construction industry is embracing digital transformation and new technologies. \
    Building Information Modeling (BIM), drones, and 3D printing are being used to improve project efficiency and quality. \
    The industry is also focusing on sustainability, with green building practices and materials gaining traction. \
    The adoption of technology is helping to address challenges such as labor shortages and project delays. \
    Despite these advancements, the industry faces obstacles related to regulation, cost, and adoption.",

    "The media industry is navigating the shift to digital and the changing landscape of content consumption. \
    Traditional media companies are adapting to new platforms and business models. \
    Social media and user-generated content are playing a significant role in shaping public discourse. \
    The industry is also grappling with issues related to misinformation, privacy, and regulation. \
    Despite these challenges, there are opportunities for innovation and growth in the digital age.",

    "The real estate industry is evolving with the integration of technology and data analytics. \
    Proptech solutions are enhancing property management, transactions, and tenant experiences. \
    The use of AI and big data is enabling better decision-making and efficiency. \
    The industry is also focusing on sustainability and smart buildings. \
    However, there are challenges related to regulation, data privacy, and market dynamics.",

    "The logistics and supply chain industry is undergoing a transformation with the adoption of technology. \
    Automation, IoT, and blockchain are being used to improve efficiency and transparency. \
    The industry is also focusing on sustainability and resilience in the face of disruptions. \
    E-commerce growth is driving changes in logistics operations and last-mile delivery. \
    Despite these advancements, the industry faces challenges related to infrastructure, regulation, and workforce development."
]

headlines = [
    "Stock Market Soars with Major Gains",
    "Government Announces Historic Carbon Emission Policy",
    "New Treatment for Rare Disease Discovered",
    "Race for AI Dominance Heats Up",
    "Community Celebrates Annual Festival",
    "Renewable Energy Sector Experiences Rapid Growth",
    "Biotechnology Advances Lead to New Medical Treatments",
    "Transportation Industry Transformed by Autonomous Vehicles",
    "Financial Sector Embraces Blockchain Technology",
    "Education System Evolves with Digital Tools",
    "Healthcare Industry Leverages Big Data for Better Outcomes",
    "Urgent Action Needed to Combat Climate Change",
    "Agricultural Sector Adopts New Technologies",
    "Retail Industry Transformed by E-commerce",
    "Entertainment Industry Evolves with Streaming Services",
    "Space Industry Enters New Era of Exploration",
    "Hospitality Industry Adapts to Changing Consumer Preferences",
    "Fashion Industry Embraces Sustainability and Innovation",
    "Energy Sector Shifts Towards Renewable Power",
    "Automotive Industry Embraces Electric Vehicles",
    "Food and Beverage Industry Evolves with Consumer Trends",
    "Travel Industry Rebounds with New Health Protocols",
    "Telecommunications Industry Advances with 5G",
    "Construction Industry Embraces Digital Transformation",
    "Media Industry Navigates Shift to Digital",
    "Real Estate Industry Integrates Technology and Analytics",
    "Logistics Industry Transforms with Technology Adoption"
]
