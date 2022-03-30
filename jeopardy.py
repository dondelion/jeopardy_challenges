import pandas as pd
pd.set_option('display.max_colwidth', None)

## explore data set

jeopardy_data = pd.read_csv('jeopardy.csv')
# print(jeopardy_data.columns)

def clean_tag(data):
  cleaned_tag = []
  for i in data.columns:
    cleaned_tag.append(i.strip())
  return cleaned_tag
jeopardy_data.columns = clean_tag(jeopardy_data)

# now headers are clean (with no blank space)
# print(jeopardy_data.columns)

def filter_data(data,words):
  filter_fx = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data.Question.apply(filter_fx)]
# dataset whose question are comprised with King and England (keywords)
king_england_data = filter_data(jeopardy_data, ['King','England'])
# print(king_english_data.Question.count())
## add float colunm to be calculated
jeopardy_data['Float_value'] = jeopardy_data.Value.apply(lambda x: float(x[1:].replace(",","")) if x!= "None" else 0)

king_data = filter_data(jeopardy_data, ['king'])
## an avg price of questions with keyword 'king' 
# print(king_data.Float_value.mean())

def get_unique_answer(data):
  return data.Answer.value_counts()
# after fx declared, try put king_data (dataset in it)
# print(get_unique_answer(king_data))

#challenge #1
filtered = filter_data(jeopardy_data ,['Computer'])
filtered_1990s = filtered[(filtered['Air Date'] >='1990-00-00') & (filtered['Air Date'] <'2000-01-01')]
filtered_2000s = filtered[(filtered['Air Date'] >='2000-00-00') & (filtered['Air Date'] <'2009-12-31')]

# print(abs(filtered_1990s['Question'].count() - filtered_2000s['Question'].count()))

#challenge #2
new_df = jeopardy_data.groupby(['Category','Round']).Question.count().reset_index()

pivot_version = new_df.pivot(columns='Round', index='Category', values='Question')

# print(pivot_version)

#challenge #3 Generate a quiz from dataset , take a user's input, and then return if it's correct?
import random
def get_quiz(data):
  random_row = random.randint(0,len(data))
  question = data.iloc[random_row] #### uncomment below to unlock the answer (cheat mode)
  a_question = question.Question + "?" ##+ question.Answer
  return a_question, question
def get_answer():
  answer = input("enter your answer here..")
  return answer
def play_quiz(data):
  quiz, question = get_quiz(data)
  print(quiz)
  ans = get_answer()
  if ans == question.Answer:
    return "You are Great!"
  else:
    return "Until Next time.."

play_quiz(jeopardy_data)