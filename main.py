import os
import openai

# API-ключ
api_key = 'тут був апі ключ' # видалив з ціллю безпеки
os.environ["OPENAI_API_KEY"] = api_key

def get_chatgpt_response(prompt):
    try:
        client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return chat_completion.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    user_prompt = input("Введіть ваш промпт: ")
    response = get_chatgpt_response(user_prompt)
    print("ChatGPT:")
    print(response)

if __name__ == "__main__":
    main()
