This datasheet follows the Aether Data Docmentation template. The datasheet/data I worked with is the norman pd files, specifically with the incident summary files and can be found at https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports

BASICS: CONTACT, DISTRIBUTION, ACCESS
1. Dataset name
The dataset we are dealing with is the Norman Oklahoma Police Department webpage. 

2. Dataset version number or date
Present day(They keep updating webite every month with the case summaries, incidents and arrests happening on each day of that month.)

3. Dataset owner/manager contact information, including name and email
Dataset manager/ownder -> Norman PD IT team
Contact information: 405-321-1444(Non-emergency)
Email:  pdprofstandards@normanok.gov

4. Who can access this dataset (e.g., team only, internal to the company, external to the
company)?
This information is made public and can be accessed by anyone. 
You can use their link : https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports

5. How can the dataset be accessed?
One way to access dataset is by utilizing link and downloading the PDFs. 

DATASET CONTENTS
6. What are the contents of this dataset? Please include enough detail that someone unfamiliar
with the dataset who might want to use it can understand what is in the dataset.
Specifically, be sure to include:
- What does each item/data point represent (e.g., a document, a photo, a person, a
country)?
- How many items are in the dataset?
- What data is available about each item (e.g., if the item is a person, available data
might include age, gender, device usage, etc.)? Is it raw data (e.g., unprocessed text or
images) or features (variables)?
- For static datasets: What timeframe does the dataset cover (e.g., tweets from January
2010–December 2020)?
The website contains many reports showing the crime and other related data for that city.Since this project only works with incident_summary pdfs, I will focus on that. For everyday of the month a daily incident summary file highlights the incidents that took place on that day. For each day you have the following details:
Date/Time of incident
Incident Number
Location
Nature of Incident
Incident ORI
One page has 16 entries and each pdf might have roughly 25 pages resulting in around 400 entries. Timeframe of data available for each month is from 2022 to present.

INTENDED & INAPPROPRIATE USES
7. What are the intended purposes for this dataset?
This is public data. It could be used for various purposes like analyzing which area and what time crime usually happens, what kind of crime is most common etc. Could also be used for NLP tasks like POS tagging. 

8. What are some tasks/purposes that this dataset is not appropriate for?
In my opinion using this for prediction tasks might be a double edged sword as it will start including bias. It comes down to how a user implements their predictions. 

DETAILS
DATA COLLECTION PROCEDURES
9. How was the data collected?
Describe data collection procedures and instruments.
Describe who collected the data (e.g., contractors).
Data was collected after every record of an arrest or incident goes to the record. I am guessing data was maintained by the IT team after any incident to make sure they match with their private database that might contain more details associated with the individual. However how exactly they were collected, I do not know. 

10. Describe considerations taken for responsible and ethical data collection (e.g., procedures, use
of crowd workers, recruitment, compensation).
Since this is data collected by police department, it might not involve traditional data collection procedures. 

11. Describe procedures and include language used for getting explicit consent for data collection
and use, and/or revoking consent (e.g., for future uses or for certain uses). If explicit consent
was not secured, describe procedures and include language used for notifying people about
data collection and use.
Since this is public data that does not contain any information about protected groups there is no requirement to ask for any consent. 

REPRESENTATIVENESS
12. How representative is this dataset? What population(s), contexts (e.g., scripted vs.
conversational speech), conditions (e.g., lighting for images) is it representative of?
How was representativeness ensured or validated?
What are known limits to this dataset’s representativeness?
Since the aim was to record instances of crime from one particular city/town it is just a collection of incidents. There is no representation explicitly needed. 

13. What demographic groups (e.g., gender, race, age, etc.) are identified in the dataset, if any?
How were these demographic groups identified (e.g., self-identified, inferred)?
What is the breakdown of the dataset across demographic groups? Consider also reporting
intersectional groups (e.g., race x gender) and including proportions, counts, means or other
relevant summary statistics.
Note: This information can help a user of this dataset understand what groups are represented in
the dataset. This has implications for the performance of models trained on the dataset and on its
appropriateness for fairness evaluations – e.g., comparisons of performance across groups.
This particular dataset does not deal with identity associated with any individual. All of the data is related to location. So if any bias were to be available it would be related to location of the incident and not an individual. 

DATA QUALITY
14. Is there any missing information in the dataset? If yes, please explain what information is
missing and why (e.g., some people did not report their gender).
Note: Consider the impact of missing information on appropriate uses of this dataset.
Few pdfs have empty cells. I am not sure if those indicate records of few people being removed for certain reasons. But the instance of this happening is very rare. 

15. What errors, sources of noise, or redundancies are important for dataset users to be aware of?
Note: Consider how errors, noise, redundancies might impact appropriate uses of this dataset.
Some empty cells might impact user activity. Usually a simple try and except or some other logic will take care of it. 

16. What data might be out of date or no longer available (e.g., broken links in old tweets)?
Data of all arrsts and incidents that is posted works fine. 

17. How was the data validated/verified?
Since it was maintained by the police department, I did not verify anything. I just hope if there was some issues like wrongful arrest, the records are eventually updated to exclude the names of the innocent. 

18. What are potential validity issues a user of this dataset needs to be aware of (e.g., survey
answers might not be truthful, age was guessed by a model and might be incorrect, GPA was
used to quantify intelligence)?
Since this data is updated and mainted by department of Norman, the details regarding incidents have to be true. However that does not account for any wrongful arrests that may have taken place and those issues I am not sure how a user can verify. 

19. What are other potential data quality issues a user of this dataset needs to be aware of?
PRE-PROCESSING, CLEANING, AND LABELING
Some of the pdfs have empty cells. So upto the user on how they want to handle it. 

20. What pre-processing, cleaning, and/or labeling was done on this dataset?
Include information such as: how labels were obtained, treatment of missing values, grouping
data into categories (e.g., was gender treated as a binary variable?), dropping data points.

Who did the pre-processing, cleaning, and/or labeling (e.g., were crowd workers involved in
labeling?)
Note: Consider how this might impact appropriate users of this dataset (e.g., binary gender might
be insufficient for fairness evaluations; imputing missing values with the mean may create
anomalies in models trained on the data).
NIL.

21. Provide a link to the code used to preprocess/clean/label the data, if available.
NIL. 

22. If there are any recommended data splits (e.g., training, development/validation, testing),
please explain.
I did not perform any ML task with these so I am not sure. Besides I dont think making predictions based on where incidents have happened is a good idea as it is very likely to introduce some bias. 

PRIVACY
23. What are potential data confidentiality issues a user of this dataset needs to be aware of?
How might a dataset user protect data confidentiality?
Since this is data made for public, confidentiality is not really a thing. However I dont think there is any very sensitive data that gives details regarding a specific person. Just contains information pertaining to where incident occured and what the incident was. 

24. Is it possible to identify individuals (i.e., one or more natural persons), either directly or
indirectly (i.e., in combination with other data) from the dataset?
Does the dataset contain data that might be considered sensitive in any way (e.g., data that
reveals race, sexual orientation, age, ethnicity, disability status, political orientation, religious
beliefs, union memberships; location; financial or health data; biometric or genetic data;
criminal history)?
In this data, there is no name, age, gender or any other columns. Just details regarding what the incident is and where it took place. I am assuming they have another privae database consisting of the names of people related to the incidents here. It will contain sensitive data but I dont think that information is made available to the public. 

If the answer to either of these questions is yes, please be sure to consult with a privacy expert
and receive approvals for storing, using, or distributing this dataset.
25. If an analysis of the potential impact of the dataset and its uses on data subjects (e.g., a data
protection impact analysis) exists, please provide a brief description of the analysis and its
outcomes here and include a link to any supporting documentation.
There is no official analysis on the mpat these records have left. However there have been analysis done by many in the past to see the which policing practices have patterns of racial disparities, and what factors may be contributing to those disparities. Link: https://justicenavigator.org/report/norman-city-ok-2021/summary

26. If the dataset has undergone any other privacy reviews or other relevant reviews (legal,
security) please include the determinations of these reviews, including any limits on dataset
usage or distribution.
There is no limits explicitly mentioned. However doing too many API calls in a short span of time will get you blocked by them. I am not sure exactly how many calls is the usage limit though. 

ADDITIONAL DETAILS ON DISTRIBUTION & ACCESS
27. How can dataset users receive information if this dataset is updated (e.g., corrections,
additions, removals)?
I dont think there is any newsletter or subscription available. However simply by regularly checking the website people will be able to tell the updations. Although this has led me to think if incase of any inncoment person getting charged, their name will be removed from past records. Ideally that would be the case. 

Note: Consider creating a distribution list people can subscribe to.
28. For static datasets: What will happen to older versions of the dataset? Will they continue to be
maintained?
29. For streaming datasets: If this dataset pulls telemetry data from other sources, please specify:
- What sources
- How frequently the dataset is refreshed
- Who controls access to these sources
- Whether access to these sources will remain available, and for how long
- Any applicable access restrictions to these sources including licenses and fees
- Any other available access points to these sources
- Any relevant information about versioning
Are there any other ways in which these sources might affect this dataset that a dataset user
needs to be aware of?


30. If this dataset links to data from other sources (e.g., this dataset includes links to content such
as social media posts or, news articles, but not the actual content), please specify:
- What sources
- Whether access to these sources will remain available, and for how long
- Who controls access to these sources
- Any applicable access restrictions to these sources including licenses and fees
- For static datasets: If an official archival version of the complete dataset exists (i.e.,
including the content as it was at the time the dataset was created), where it can be
accessed
Are there any other ways in which these sources might affect this dataset that a dataset user
needs to be aware of?
This dataset is not directly involved with any other data. However some records might contain information from this data as well. For example if in a criminal incident if anyone were to get hurt, the incident ORI detials would also be stored in the hospital database. 

31. Describe any applicable intellectual property (IP) licenses, copyright, fees, terms of use, export
controls, or other regulatory restrictions that apply to this dataset or individual data points.
These might include access restrictions related to data subjects’ consenting or being notified of
data collection and use, as well as revoking consent.
Provide links to or copies of any such applicable terms.
None as far as I know. Since this is all data that is made available to the public there is little reason for licensing to be involved. However a large number of API calls will get you blocked for a temporary amount of time. 