from openai import OpenAI

from configuration.configuration import AppConfig
from context.story_context import StoryPrompt, ChooseYourOwnStoryPrompt

CONFIG_FILE = "config.json"

config = AppConfig(config_file=CONFIG_FILE)
prompt = ChooseYourOwnStoryPrompt()

client = OpenAI(base_url=config.llm_base_url, api_key=config.llm_api_key)

completion = client.chat.completions.create(
  model=config.llm_model,
  messages=[
    {"role": "system", "content": prompt.system_prompt()},
    {"role": "user", "content": prompt.user_prompt()}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)