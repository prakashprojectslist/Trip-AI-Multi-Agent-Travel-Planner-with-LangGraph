from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


'''res = search_flights("plan a 7 days Japan trip from india")
print(res)'''


result = run_travel_agent("plan a 7 days Japan trip from india")
print(result)


user_input = input("Enter your travel query: ")

response = run_travel_agent(user_input=user_input, thread_id="test_user")

print("\n Final Response:\n")                     
print(response["answer"])




