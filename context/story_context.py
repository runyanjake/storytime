class StoryPrompt:

    def system_prompt(self):
        return 'You are an AI designed to output efficient Python code with perfect syntax.'

    def user_prompt(self):
        return 'Write a Hello World program in Python.'
    

class ChooseYourOwnStoryPrompt(StoryPrompt):

    def system_prompt(self):
        return '''
            You are an AI designed to create interactive, choose-your-own-adventure style stories.
        '''

    def user_prompt(self):
        return '''
            Generate the first page of a choose-your-own-adventure style story.
            Your response should be exactly 4-8 sentences that describe an engaging scenario and end with a choice. 
            The last sentence should present two options for the user to choose from. Ensure the story is 
            imaginative and intriguing. End your response with a question asking the user which of the two 
            options they would like to take."
        '''