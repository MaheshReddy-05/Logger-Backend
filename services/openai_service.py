import openai

openai.api_key = "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"

def get_solution(log_data, nearest_logs):
    nearest_logs_context = "\n".join(nearest_logs)
    prompt = (
        f"The following log error was received:\n{log_data}\n\n"
        f"Here are two previously solved similar logs:\n{nearest_logs_context}\n\n"
        "Using your knowledge base and the information above, "
        "analyze the error and provide a clear explanation of the issue and "
        "suggest detailed steps to resolve it."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in diagnosing and resolving log errors."},
                {"role": "user", "content": prompt}
            ]
        )

        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        print(f"OpenAI API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

