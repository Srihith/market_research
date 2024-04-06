import openai
import os

# Replace 'your_openai_api_key_here' with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')

def ai_market_research_agent(conversation):
    """
    This function takes the full conversation as input and uses OpenAI to continue the conversation, 
    considering the entire context.
    """
    try:
        # Call the OpenAI API with the conversation history
        response = openai.Completion.create(
            engine="text-davinci-003",  # or the latest version available
            prompt=conversation,
            temperature=0.7,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None  # You might want to specify stopping criteria depending on your conversation format
        )

        # Print the AI's response
        print("AI Response:")
        print(response.choices[0].text.strip())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize an empty conversation
    conversation = """
    Objective: Gather as much infromation as possible from the user about finance appications. The company you are doing research for is called Alffin. This is similar to Mint.com. 
    Mint.com is an online personal finance tool that allows you to track your spending and helps you make a budget. Mint is a free service. 
    If you want to use Mint, you must sync all of your financial accounts, or at least the ones you want to utilize via Mint. The difference between Alffin and Mint is 1. Alffin allowed you to
    connect your brokerage and buy / sell stocks 2. Give you financal product at a better rate once once you have connected your accounts. Your goal to see if users care about either of these use cases.

    
    As an AI market research expert, provide detailed market research findings on the above objective.
    """

    # Simulate user response
    user_response = "What are the major challenges facing the electric vehicle market?"

    # Update conversation with user's response
    conversation += f"\nUser: {user_response}\nAI:"

    # Call the AI market research agent with the updated conversation
    ai_market_research_agent(conversation)
