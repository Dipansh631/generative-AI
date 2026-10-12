from typing import Literal
print("[1/3] Loading environment variables and importing libraries...", flush=True)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Literal
load_dotenv()
from pydantic import BaseModel, EmailStr,Field
from typing import Optional

print("[2/3] Connecting to Gemini API and initializing model...", flush=True)
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.2)
class Review(TypedDict):
    key_themes:list[str]=Field(default=None, description="write down all Key themes in the review discussed in review")
    summary:list[str]=Field(default=None, description="write down a summary of the review")
    sentiment:Literal['Positive','Negative']=Field(description="The sentiment of the review either positive or negative")
    pros:Optional[list[str]]=Field(default=None, description="write down all pros of the review")
    cons:Optional[list[str]]=Field(default=None, description="write down all cons of the review")
    name:Optional[str]=Field(default=None, description="write down the name of the product being reviewed")
Structured_model=model.with_structured_output(Review)

print("[3/3] Sending request to Gemini (this may take 5-15 seconds depending on connection)...", flush=True)
result=Structured_model.invoke("""I purchased this charger three weeks ago to replace the separate bricks I was carrying for my laptop, tablet, and phone. Overall, it has significantly cleaned up my workspace and reduced the weight of my travel bag.What I Like:Power Delivery: It easily powers my 16-inch laptop and fast-charges my phone at the same time without any noticeable drop in performance.Compact Design: Thanks to the GaN technology, it is roughly half the size of my older laptop charger. The foldable prongs are a massive plus for traveling.Port Variety: Having three USB-C ports and one USB-A port allows me to charge all my daily devices simultaneously.What to Consider:Heat Generation: When utilizing the full 100W output with multiple devices plugged in, the brick gets noticeably hot to the touch. It hasn’t shut down due to overheating, but it is something to watch out for.Port Allocation: The power distribution changes depending on which ports you use. If you plug in a small accessory, it sometimes temporarily resets the connection on the other ports to reallocate the wattage.Final Verdict:If you need a single, powerful hub for a multi-device setup, this is an excellent choice. Just ensure it is placed in a well-ventilated area if you plan to max out its charging capacity.""")

print("\n--- Result Received ---", flush=True)
print(result, flush=True)
print(result.sentiment)
print(result.pros)
print(result.cons)
print(result.key_themes)




    