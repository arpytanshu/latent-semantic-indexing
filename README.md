# latent-semantic-indexing
This Latent Semantic Indexing [ LSI ] model collects, parses, and stores documents to facilitate fast and accurate information retrieval through queries.

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

