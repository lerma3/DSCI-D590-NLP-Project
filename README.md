# The Facebook Campaign: Revealing Politcians’ Hidden Ads

## Kevin Fosnacht & Rosemarie Lerma
## Final project for DSCI - D590 - Intro to NLP

### Objectives
In 2007, Barak Obama utilized social media to run for office and that was a game changer. Until Obama utilized MySpace.com, political campaigns were contained within the television, radio, and print media spaces. Political ads were systematic, they exercised message discipline and message control (Perlmutter, 1999; Stromer-Galley, 2000). As political parties have become more polarized, their ideological underpinnings have manifested themselves in the ads. The advent of microtargeting that social media has made easy for campaigns allows campaigns to disseminate different messages to different groups. Consequently, campaign messaging has transformed from a collective to an individual message. 
As the 2022 mid-term elections loom, what do campaign ads look like? This project utilizes campaign ads on Meta (Facebook, Instagram, Whatsapp) platforms from candidates running for the U.S. Senate in 2022. This project will unveil the varying messages disseminated by the platform using Natural Language Processing techniques. First, the campaign ads will apply keyword extraction to understand what key phrases appear most often in the ads. Also, the program will identify the sentiment of ads to obtain the average tone used. By using keyword extraction and sentiment analysis, this project will provide a robust understanding of the look and feel of social media campaign ads today through identifying the most common key phrases and the degree of negative campaigning.

### Keywords 
social media, campaign ads, sentiment analysis, keyword extraction

### Usefulness
Due to the high degree of ad targeting used in modern campaigns, it is difficult for voters and journalists to understand and comprehend the scope of campaign messaging. This project seeks to shine light into this new and dark area of modern campaigning by converting the thousands of add permutations campaigns create and distill the findings into something digestible for a typical voter. In particular, we will report the most common keywords used in the ads and their sentiment to report the extent of negative campaigning. To aid in voters’ decisions, we will display the results

### Data
The project data will be derived from Meta’s (2022) ad library. We will be focusing on the ad_creative_bodies field in the library, which is the body of the ad disseminated by the campaign, the ad titles (ad_creative_link_titles), and link captions (ad_creative_link_captions).
  
### Analyses

This project will help illuminate the hidden campaign by summarizing the ad texts through wordclouds based on TF-IDF vectorization and the degree of negative campaigning by calculating ad sentiment using the AFINN algorithm.

