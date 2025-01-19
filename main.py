import pandas as pd
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import csv


load_dotenv()


class bot:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=os.environ['api']
        )
        self.docs = 'items.csv'  # this should load dynamically
        self.agent = create_csv_agent(
            llm=self.llm,
            path=self.docs,
            verbose=True,
            allow_dangerous_code=True
        )
        self.main_commands()  # call to main command when we initiate the program

    def main_commands(self):
        # main command options for users
        print(f'\n1. Enter query\n2. Load another data file\n3. print dataset\n4. Exit\n')
        user_input = input('select option number : ')
        if user_input == '1':
            self.user_quary()
        elif user_input == '2':
            self.load_csv()
        elif user_input == '3':
            self.print_dataset()
        elif user_input == '4':
            self.exit_query()
        else:
            print('invalid input')
            self.main_commands()

    def check_datatype(self, data):
        # check the data type of the selected file - csv or not
        try:
            pd.read_csv(data)
            return True
        except:
            return False

    def load_csv(self):
        # upload new csv dataset
        csv_file_path = input('select csv file path : ')
        if (os.path.exists(csv_file_path) and self.check_datatype(csv_file_path)):
            self.docs = csv_file_path
            self.agent = create_csv_agent(
                llm=self.llm,
                path=self.docs,
                verbose=True,
                allow_dangerous_code=True
            )
            self.main_commands()
        else:
            print('file not found or file type is not matching')
            print(f'1. try agian\n2. go to main commads\n')
            user_input = input('select your coice again : ')
            if int(user_input) == 1:
                self.load_csv()
            elif int(user_input == 2):
                self.main_commands()
            else:
                print('invalid input')
                self.main_commands()

    def user_quary(self):
        # get user queries and return the response from query native language
        query = input('Enter your query : ')
        response = self.agent.run(
            query + 'use input language as a output language')
        print(response)
        self.main_commands()

    def print_dataset(self):
        # print csv dataset
        data_set = pd.read_csv(self.docs)
        print(f'\n{data_set}\n')
        self.main_commands()

    def exit_query(self):
        # exit from the dataset
        exit()


bot()
