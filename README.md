# BATTLE OF NEIGHBOROOHS
Applied Data Science Capstone
Peer-graded Assignment: Capstone Project - The Battle of Neighborhoods
# I. Introduction (Business Problem)
Coffee shop is one place that people can go to, whether for quick refreshment, truly enjoying the 
coffee, or becoming temporary workspace for individuals.
According to the research by Toffin and MIX MarComm SWA Media Group magazine, the number 
of coffee shops in Indonesia has reached 2,950 in 2019, which was 3x compared to 2016. This 
phenomenon was drived by many factors, such as presence of social media than eases promotion, 
existence of ride hailing platforms that can ease customers to purchase via delivery, increasing 
purchasing powers, and new culture of hanging out among youngsters in Indonesia.
Businessmen and women who are interested in building new brands of coffee shop, or franchise, 
should assess every aspect thoroughly as a part of business plan, so the business can profit as much 
as possible. One aspect that can affect the profit is the location. Building coffee shops in a region 
full of competitors can be tough, so one can opt to strategize by opting regions with a greater
number of populations yet a smaller number of rivals.
Bandung, as now populated by 2.5 million of people, is now the 4th most populated cities in 
Indonesia, having no exception to this increasing trend of coffee shops. This assignment is for 
businessmen or women who are interested in building new brand of coffee shops or expanding 
their brands in Bandung. To summarize, where should someone/a company have a new 
branch/make new local brand of coffee shop in Bandung?
# II. Data
First Data is taken from Open Data Kota Bandung. The data taken from this website is the number 
of populations in Bandung based on age groups and neighbourhoods (or "Kecamatan" in 
Indonesian terms). From this data, the age groups will be reorganized into new groups (children, 
teenagers, young adults, adults, and senior adults). The number of young adults & adults’
population per Kecamatan will be included as features.
The other data is taken from FourSquare API, in which venues in each Kecamatan will be collected, 
and the number of coffee shops per Kecamatan will be included as feature too.
# III. Methodology
A. Exploratory Data Analysis in Bandung Population Dataset
First, let’s see how the population dataset looks like
Figure 1 – Snapshot of Bandung Population Dataset 
 
Dataset contains of 151 rows and 18 columns. In this dataset, name of Kecamatan and Kelurahan 
(borough/smaller regions under it) are also included. The number population is categorized into 
several age groups in range of 5 years. For the project, the dataset will be recategorized into new 
age groups. In Bandung, there are 30 Kecamatans as the object of analysis.
Figure 2 – Number of Kecamatan in Bandung
For all the 30 Kecamatans in Bandung, let’s see total population for each Kecamatan.
Figure 3 – Left: Total Population per Kecamatan, Right – Statistical Description of Total Population per Kecamatan
The most populated Kecamatan in Bandung is Babakan Ciparay, with around 139,000 persons, 
while the least populated is Cinambo (around 25,000 persons). Average total population is around 
83,000 persons. 
Figure 4 – Left: Total Population Based on Old Age Group, Right: Total Young Adults & Adults per Kecamatan
 
The dataset is recategorized into new age groups with specification:
- Children: 0-9 years old
- Teenagers: 10-19 years old
- Young Adults: 20-29 years old
- Adults: 30-49 years old
- Senior adults: > 49 years old
According to the charts above, Bandung is dominated with Adults age group, followed by Senior 
Adults. Bandung has big potential for coffee shops expansion, since the number of populations of 
Adult & Young Adult is quite high. Kecamatan with highest number of adults and young adults are 
Babakan Ciparay, Kiaracondong, and Bandung Kulon.
B. Exploratory Data Analysis in Bandung Venues
In this part, the venues per Kecamatan will be retrieved using Foursquare API. First, we will retrieve 
the coordinate of each Kecamatan through geocoder libary. The coordinate of Bandung will also 
be retrieved.
Figure 6 – Snapshot of Venue Dataset
Figure 5 – Population Based on New Age Group
According to the picture above, there are 2501 venues collected around Bandung. Radius is set as 
3000 and limit of total venues collected per request is 100.
Figure 8 – 10 Most Common Venues in Bandung
According to the chart above, it seems that there are some more crowded Kecamatans, where, in 
terms of business/number of venues, they have 100 as maximum values. The others are less 
crowded. There are 167 unique categories of venues in total.
It also can be concluded that Indonesian Restaurant has been the most common venue categories
in most of Kecamatans in Bandung, followed by Hotels. Meanwhile, in terms of number of venues 
per category, Hotel is the most common venues, followed by Coffee Shop and Indonesian 
Restaurant.
C. Machine Learning Algorithms Used
In this project, we will discover Kecamatans in Bandung that are suitable for people who want to 
expand their business in coffee shops, by using K-Means clustering with the features of number of 
existing coffee shops and total populations of adults and young adults per Kecamatan.
The reason of selecting these features are that we want to minimize the possibilites of 
competitions in the same area and maximize the purchases by selecting areas having more people 
Figure 7 – Left: Number of Venues per Kecamatan, Right: 
Most Common Venues per Kecamatan
with higher possibilities in purchasing powers and eagerness to spend money or time in coffee 
shops, hence the young adults and adults.
Features will be clustered into 3 groups by using K-Means. The reason of applying this algorithm is 
features are quite simple, so the process will be quicker yet easier to interpret.
# IV. Analysis and Results
A. Pre-Processing
First, for every venue that have been retrieved, we will create one-hot encoding based on the 
venue type. Then, for each Kecamatan, we will count the average of each venue type, so that we 
can get the representation of total venue type per Kecamatan as features. For further analysis, we 
also create 10 most common venue types per Kecamatan.
Figure 9 – Snapshots of Derived Features
The features that will be included for clustering is Averaged number of coffee shop and total young 
adults & Adults population per Kecamatan. The reason why these age groups are included is that 
adults have the purchasing power and some of young adults may have too, but they have the 
eagerness to spend time and money in the coffee shop. The population features will be scaled 
before clustering.
Figure 10 – Snapshot of Final Features
B. Result
Figure 11 – Clusters of Kecamatan based on K-Means
Cluster 0 is denoted by red, 1 is purple, 2 is light green.
According to the result above, Cluster 0 has the most Kecamatans and Cluster 2 has the least ones. 
Most of the Kecamatans in Cluster 2 are in the eastern Bandung, while Cluster 1 tends to be in
central-western Bandung. Meanwhile Cluster 0 is spread around the city.
Figure 12 - Characteristics of Cluster 0
Figure 13 - Characteristics of Cluster 1
Figure 14 - Characteristics of Cluster 2
Looking at the screenshots of each clusters, it seems the clusters are highly dependant on targeted 
population rate. Cluster 2 has the least number of young adults and adults, meanwhile Cluster 1 
has the highest number. 
To sum up how dominant coffee shops in each Kecamatan, we can see the table below.
Clusters Number of Kecamatan with Coffee Shops as
1
st Most Common 
Venues
2
nd Most
Common Venues
3
rd Most
Common Venues
Cluster 0 2 2 2
Cluster 1 3 1 0
Cluster 2 1 1 1
Table 1 – Number of Kecamatans with Coffee Shops as 3 Most Common Venus
According to the table above, we can find coffee shops most easily in Kecamatans of Cluster 0 since
it has been on the top 3 most common venues of most Kecamatan in cluster 0. Cluster 2 does not 
really have a lot of coffee shops among the clusters.
# V. Discussion
It can be concluded that the clusters are clearly built based on the total of populations first, then 
followed by the number of coffee shops.
For recommendation of where to build new coffee shops, people should choose Kecamatans in 
Cluster 1, since this cluster has the highest rate of adults & young adults but have moderate 
numbers of coffee shops.
If to be detailed, I would further recommend the Kecamatans also based on location near the city 
center/most visited place or from Cluster 1. In Bandung, most hang out/visited places are in city 
center towards the north.
Here are top 3 Kecamatans in cluster 1 for building new coffee shops:
1. Kiaracondong (targetted population is around 0.9, coffee shop is the 5th most common place)
2. Batununggal (targetted population is around 0.8, coffee shop is the 4th most common place)
3. Coblong (targetted population is around 0.73, coffee shop is the 4th most common place, region 
is often visited)
# V. Conclusion
Coffee shop is one example of top growing business in Indonesia that targets young adults and 
adults as the consumers. Bandung, the 4th biggest city in Indonesia is also an interesting target for 
businessmen/women who intends to expand their coffee shop business, since Bandung has 
supportive demographic of targeted customers.
Using K-Means, neighborhoods or Kecamatans in Bandung are clustered into 3 clusters based on 
the total of targeted populations and number of coffee shops. The clusters derived from the KMeans are clearly built on the total targeted population first, in which the Cluster 1 has the highest 
rate of targeted population and also least amount of Kecamatans that have coffee shops as the 
most common venues.
Kiaracondong, Batununggal, and Coblong are three recommended Kecamatans from Cluster 1, 
since they have the combination of highest rate of targeted population, amount of coffee shops, 
and the location near the city center/most visited places.
My suggestions for further development are:
1. Leveraging other dataset that contains income rate per Kecamatan, to add the knowledge on 
purchasing power
2. Include data about location/Kecamatans with traffic jams rate, since this may affect delivery 
punctuality
3. Numbers of ratings submitted to Google or ride hailing app, to give an insight on purchase 
rates in the area, or even the rating themselves can provide knowledge on where to compete 
easier.
