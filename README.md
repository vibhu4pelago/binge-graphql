# binge-graphql
Graphql version of a tiny part of a cinephiles' app

The app is a social media platform where people can book watch parties for movies, review and share them.

So the app has different home tab screens:
- Movies List
- Movie Details Page
- Reviews Section
- My Bookings

Parts of different models render on different screens as well.
Fetching the apt content for different screens fits a good use case of using GraphQL.

### How to run
1. Build the docker image: `./docker_build.sh`
2. Run the container `docker run -d -p 5000:5000 --name=binge-graphql binge-graphql`

Access GraphiQL interface on host's http://127.0.0.1:5000/graphql

Note: The DB would be ephemeral just like the container as it'd a sqlite DB within the container.
If we want to make it persistent we can mount a volume on to the container and adjust the db path in app accordingly.

### Learnings
- **GraphQL** - Awesome way to give more control to client and have a clear schema
  - HTTP verbs have a reduced meaning in GraphQL compared to REST APIs. Almost all requests (both Query and Mutations) goes through POST
  - **Relay**: Nodes/edges concept for pagination, sorting, filtering etc.
  - interfaces, unions, fragments
- **sqlalchemy** - I've used Django models extensively, but this is more lower level and relationships like FK are handled differently (also, composite keys)
- **graphene** - Python library for supporting GraphQL. It has all the flexibility for further extensions and stuff
- **graphene_sqlalchemy** - A wrapper to provide out-of-the-box G-QL objects if we have sqlalchemy models

### Thoughts & Doubts:
- User based serialized fields in response? Is there a better way than using Unions?
- Different mutations for Create, Update and Delete?
