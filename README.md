# binge-graphql
Graphql version of a tiny part of a cinephiles' app

So the app has different home tab screens:
- Movies List
- Movie Details Page
- Reviews Section
- My Bookings

Parts of different models render on different screens as well.
Fetching the apt content for different screens fits a good use case of using GraphQL.

### Learnings
- **GraphQL** - Awesome way to give more control to client and have a clear schema
  - HTTP verbs have a reduced meaning in GraphQL compared to REST APIs. Almost all requests (both Query and Mutations) goes through POST
  - **Relay**: Nodes/edges concept for pagination, sorting, filtering etc.
- **sqlalchemy** - I'd used Django models, but this is more lower level and relationships like FK are handled differently (also, composite keys)
- **graphene** - Python library for supporting GraphQL. It has all the flexibility for further extensions and stuff
- **graphene_sqlalchemy** - A wrapper to provide out-of-the-box G-QL objects if we have sqlalchemy models

### Thoughts & Doubts:
  - User based serialized fields in response?
  - Different mutations for Create, Update and Delete?