# latent-semantic-indexing
This Latent Semantic Indexing [ LSI ] model collects, parses, and stores documents to facilitate fast and accurate information retrieval through queries.

#### Indexing:  
The model creates a term-document frequency matrix from the document corpus.  
It then uses SVD to get a reduced representation for all terms and documents.  
(Indexing is usually slower in LSI models. And Index needs to be refreshed everytime you add a new document. LSI models are good where corpus is not updated very frequently.)

#### Retrieval:  
The user queries are translated to vector representation using the reduced representation.  
The document vectors with the maximum cosine similarity with the query vector is fetched as result.  
(Retrieval is very fast in LSI models. Each user query translates to a vector multiplication and a lookup in a dictionay, thus the speed.)

```
after indexing ~500 documents from wikipedia, the following documents were fetched by the model for the following queries
=========================================================================================================================

QUERY: probability
top 2 response:
==>   Conditional probability  In probability theory, a conditional probability is the probability that an event will occur, when another event is known to occur or to have occurred. If the events are "A" 
==>   Philippine Fault System  The Philippine Fault System is an inter-related system of faults throughout the whole of the Philippine Archipelago, primarily caused by tectonic forces compressing the Phili

QUERY: kill animal
top 2 response:
==>   Roadkill cuisine  Roadkill cuisine is preparing and eating roadkill, animals hit by vehicles and found along roads. It is a practice engaged in by a small subculture in the United States, Southern Ca
==>   Abandoned pets  Abandoned pets are both exotic pets and companion animals that are either inadvertently or purposely cast off by their owners. This commonly occurs when an owner passes away, or when 

QUERY: yamaha
top 2 response:
==>   Production of Watchmen  Watchmen is a 2009 film based on a twelve-issue comic book limited series of same name created by writer Alan Moore, artist Dave Gibbons, and colorist John Higgins, published 
==>   Yamaha Crux  The Yamaha Crux is a 106 cc, single-cylinder four-stroke motorcycle made by India Yamaha Motor. The Crux is designed for Indian and neighboring markets. Its upgraded version is known as 

QUERY: waterfalls
top 2 response:
==>   Kailasakona Falls  Kailasakona - water falls - 80 km(Picnic spot.) Kailasakona is a beautiful perennial waterfall, situated in the Nagari valley of Chittoor District. This sacred waterfall is rich in
==>   Hidden Valley Kings  The Hidden Valley Kings is a neighborhood-based gang in Charlotte, North Carolina. It was formed in Hidden Valley, a neighborhood located between Sugar Creek Road, Interstate 85,
```



```
SAMPLE RUN

Documents Corpus:
----------------
D1 = {'d1' : 'swift is a hatchback.',
     'd2' : 'compact swift has good mileage.',
     'd3' : 'hatchback is a compact.',
     'd4' : 'compact houses are popular',
     'd5' : 'houses are expensive.',
     'd6' : 'swift sedan is expensive.',
     'd7' : 'expensive cars has less mileage.',
     'd8' : 'motorcycles have great mileage.',
     'd9' : 'motorcycles are unsafe',
     'd10' : 'stay in house if you want to be safe',
     }

User Queries:
-------------
Q = ['what is compact swift',
     'good mileage cars',
     'how to reduce expenses??']



--------------------
RESPONSE FROM MODEL:
--------------------
query : what is compact swift
result : 
compact swift has good mileage.
swift is a hatchback.

query : good mileage cars
result : 
compact swift has good mileage.
expensive cars has less mileage.

query : how to reduce expenses??
result : 
houses are expensive.
swift sedan is expensive.

```
