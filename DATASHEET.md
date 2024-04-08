This datasheet follows the Aether Data Docmentation template. 

BASICS: CONTACT, DISTRIBUTION, ACCESS
1. Dataset name

2. Dataset version number or date
3. Dataset owner/manager contact information, including name and email
4. Who can access this dataset (e.g., team only, internal to the company, external to the
company)?
5. How can the dataset be accessed?
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
INTENDED & INAPPROPRIATE USES
7. What are the intended purposes for this dataset?
8. What are some tasks/purposes that this dataset is not appropriate for?
DETAILS
DATA COLLECTION PROCEDURES
9. How was the data collected?
Describe data collection procedures and instruments.
Describe who collected the data (e.g., contractors).
10. Describe considerations taken for responsible and ethical data collection (e.g., procedures, use
of crowd workers, recruitment, compensation).

11. Describe procedures and include language used for getting explicit consent for data collection
and use, and/or revoking consent (e.g., for future uses or for certain uses). If explicit consent
was not secured, describe procedures and include language used for notifying people about
data collection and use.
REPRESENTATIVENESS
12. How representative is this dataset? What population(s), contexts (e.g., scripted vs.
conversational speech), conditions (e.g., lighting for images) is it representative of?
How was representativeness ensured or validated?
What are known limits to this dataset’s representativeness?
13. What demographic groups (e.g., gender, race, age, etc.) are identified in the dataset, if any?
How were these demographic groups identified (e.g., self-identified, inferred)?
What is the breakdown of the dataset across demographic groups? Consider also reporting
intersectional groups (e.g., race x gender) and including proportions, counts, means or other
relevant summary statistics.
Note: This information can help a user of this dataset understand what groups are represented in
the dataset. This has implications for the performance of models trained on the dataset and on its
appropriateness for fairness evaluations – e.g., comparisons of performance across groups.
DATA QUALITY
14. Is there any missing information in the dataset? If yes, please explain what information is
missing and why (e.g., some people did not report their gender).
Note: Consider the impact of missing information on appropriate uses of this dataset.
15. What errors, sources of noise, or redundancies are important for dataset users to be aware of?
Note: Consider how errors, noise, redundancies might impact appropriate uses of this dataset.
16. What data might be out of date or no longer available (e.g., broken links in old tweets)?
17. How was the data validated/verified?
18. What are potential validity issues a user of this dataset needs to be aware of (e.g., survey
answers might not be truthful, age was guessed by a model and might be incorrect, GPA was
used to quantify intelligence)?
19. What are other potential data quality issues a user of this dataset needs to be aware of?
PRE-PROCESSING, CLEANING, AND LABELING
20. What pre-processing, cleaning, and/or labeling was done on this dataset?
Include information such as: how labels were obtained, treatment of missing values, grouping
data into categories (e.g., was gender treated as a binary variable?), dropping data points.

Who did the pre-processing, cleaning, and/or labeling (e.g., were crowd workers involved in
labeling?)
Note: Consider how this might impact appropriate users of this dataset (e.g., binary gender might
be insufficient for fairness evaluations; imputing missing values with the mean may create
anomalies in models trained on the data).
21. Provide a link to the code used to preprocess/clean/label the data, if available.
22. If there are any recommended data splits (e.g., training, development/validation, testing),
please explain.
PRIVACY
23. What are potential data confidentiality issues a user of this dataset needs to be aware of?
How might a dataset user protect data confidentiality?
24. Is it possible to identify individuals (i.e., one or more natural persons), either directly or
indirectly (i.e., in combination with other data) from the dataset?
Does the dataset contain data that might be considered sensitive in any way (e.g., data that
reveals race, sexual orientation, age, ethnicity, disability status, political orientation, religious
beliefs, union memberships; location; financial or health data; biometric or genetic data;
criminal history)?
If the answer to either of these questions is yes, please be sure to consult with a privacy expert
and receive approvals for storing, using, or distributing this dataset.
25. If an analysis of the potential impact of the dataset and its uses on data subjects (e.g., a data
protection impact analysis) exists, please provide a brief description of the analysis and its
outcomes here and include a link to any supporting documentation.
26. If the dataset has undergone any other privacy reviews or other relevant reviews (legal,
security) please include the determinations of these reviews, including any limits on dataset
usage or distribution.
ADDITIONAL DETAILS ON DISTRIBUTION & ACCESS
27. How can dataset users receive information if this dataset is updated (e.g., corrections,
additions, removals)?
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
31. Describe any applicable intellectual property (IP) licenses, copyright, fees, terms of use, export
controls, or other regulatory restrictions that apply to this dataset or individual data points.
These might include access restrictions related to data subjects’ consenting or being notified of
data collection and use, as well as revoking consent.
Provide links to or copies of any such applicable terms.