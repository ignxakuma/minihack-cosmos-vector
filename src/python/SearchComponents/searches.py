# Import the necessary modules and components
import SearchComponents.vectorSearch as VectorSearch
import SearchComponents.completion as Completion
import os

# Function to run a vector search
def runVectorSearch(embeddings_deployment, AzureOpenAIClient, client, cosmos_db_mongodb_database):

    pass  
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ask the user for their query
    print("What would you like to know about our bike shop's inventory?")
    user_input = input("Prompt: ")

    # Define the maximum number of results, the vector column name, and the collection name
    maxResults = 20
    vector_column = "productVector"
    collection_name = "products"

    # Connect to the database and the collection
    db = client[cosmos_db_mongodb_database]
    collection = db[collection_name]

    # Run the vector search and print the results
    results = VectorSearch.vectorSearch(user_input, vector_column, collection, embeddings_deployment, AzureOpenAIClient, maxResults)
    for result in results:
        print(f"Similarity Score: {result['similarityScore']}"
              + f", category: {result['document']['categoryName']}"
              + f", Product: {result['document']['name']}")



# Function to run a GPT search
def runGPTSearch(embeddings_deployment, AzureOpenAIClient, completion_deployment, AzureOpenAICompletionClient, client, cosmos_db_mongodb_database):

    pass  # Replace this line with the lab's code
