 ## Setting up the Project for Development

  ### Docker Setup
  Your machine must have docker installed in it. for further guidance visit https://docs.docker.com/desktop/setup/install/linux/ubuntu/ for linux
  use similar approach for other operating system

  ### Running docker command will automatically setup the required application and database with the given settings
  sudo docker-compose up --build


### Accessing the api
  ### Health check API
  localhost:8000

  ### Playground API
  localhost:8000/graphql


### Different graphql playground queries and mutations
  ### Add Mutation
  mutation {
    addGame(gameData: {
      name: "csgo",
      type: "Technical",
      publisherName: "games",
      externalGameId: "12345",
      description: "games guide",
      isFeatured: true,
      coverImageUrl: "https://example.com/docker.jpg"
    }) {
      id
      name
    }
  }

  ### Get All Queries
  query {
  games {
    id
    name
    type
    publisherName
    externalGameId
    description
    isFeatured
    coverImageUrl
  }
}

### Retrieve single data query
query {
  game(id: "ID value") {
    id
    name
    type
    publisherName
    externalGameId
    description
    isFeatured
    coverImageUrl
  }
}

### Update data query
mutation {
  updateGame(id: "ID Value", gameData: {
    name: "Updated Name",
    type: "Updated Type",
    publisherName: "Updated Publisher",
    externalGameId: "67890",
    description: "Updated Description",
    isFeatured: false,
    coverImageUrl: "https://example.com/updated.jpg"
  }) {
    id
    name
  }
}

### Delete data query
mutation {
  deleteGame(id: "ID value")
}



