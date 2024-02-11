from bardapi import Bard
from bardapi import BardCookies
import os
from dotenv import load_dotenv

cookie_dict = {
    "__Secure-1PSID": "cwierLwWtCKRQtjSuvxkjUaSjrTNiu55EDUA7NuuS1Pq8dw_LZ9l53Mvc-Kf_UUhunu1gw.",
    "__Secure-1PSIDTS": "sidts-CjIBNiGH7jyzVA7pXb2v8NQ81tWC8fB7jSEpVn6XO9a5lXNLDjPgHwoFQhKLpbggJeWqexAA",
    # Any cookie values you want to pass session object.
}

load_dotenv()

token=os.getenv("BARD_API_KEY")
print(token)

bard = BardCookies(cookie_dict=cookie_dict)
result=bard.get_answer("Explain about pneumonia in 50 words only")

print(result["content"])

