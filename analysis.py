import argparse
import os
import json
import sys
import emoji
import pytz
import dateutil.parser
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import MWETokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from config import *
import re
from channel import Channel
from user import User

# NLTK setup
# nltk.download('popular')
stop_words = set(stopwords.words('english') + ADDITIONAL_STOP_WORDS)
# Need to reconnect some tokenized words like 'gonna'
fixer = MWETokenizer([('gon', 'na')], "")
porter = PorterStemmer()
# Set timezone
local_tz = pytz.timezone("America/Chicago")

# create a parser object
parser = argparse.ArgumentParser(description = "Discord chat analysis tool")

parser.add_argument("filepath", metavar = "file", type = str, help = "JSON file for tool to consume")
parser.add_argument("--start-date", type=lambda s: local_tz.localize(dateutil.parser.parse(s)), 
                    help = "Start date for analysis in mm-dd-yyyy format")
parser.add_argument("--end-date", type=lambda s: local_tz.localize(dateutil.parser.parse(s)), 
                    help = "End date for analysis in mm-dd-yyyy format")
  
# parse the arguments from standard input
args = parser.parse_args()

if not os.path.exists(args.filepath):
    raise FileNotFoundError(f"File {args.filepath} not found")
# Maybe check for file type?

try:
    file = open(args.filepath, "r")
    data = json.load(file)
except Exception as err:
    print(f"Could not parse JSON: {err}")
    sys.exit(1)
finally:
    file.close()

if not args.start_date:
    args.start_date = dateutil.parser.parse(data["messages"][0]["timestamp"]).astimezone(local_tz)
if not args.end_date:
    args.end_date = dateutil.parser.parse(data["messages"][-1]["timestamp"]).astimezone(local_tz)

main_channel = Channel(data["guild"]["name"], data["channel"]["id"], 
                       data["channel"]["name"], data["channel"]["topic"], 
                       data["guild"]["iconUrl"])

for message in data["messages"]:
    if not message["author"]["isBot"]:
        timestamp = dateutil.parser.parse(message["timestamp"])
        if args.start_date < timestamp.astimezone(local_tz) < args.end_date:
            main_channel.timestamps.append(timestamp.astimezone(local_tz))
            user = main_channel.get_user(message["author"]["id"])
            if not user:
                user = User(message["author"]["id"], message["author"]["name"], 
                            message["author"]["nickname"], message["author"]["avatarUrl"])
                main_channel.users.append(user)
            
            user.message_count += 1
            # Remove hyperlinks and then split message
            tokens = fixer.tokenize(word_tokenize(re.sub(r'http\S+', '', message["content"])))
            # Grabbing emojies
            user.emojis += [w for w in tokens if re.match("<?:.*:.*>?", emoji.demojize(w)) is not None]
            # convert to lower case and trim multi-letters
            tokens = [re.sub(r'(.)\1{2,}', r'\1', w.lower()) for w in tokens]

            # Remove hyperlinks from text
            # 

            # Remove remaining tokens that are not alphabetic or stop word
            words = [word for word in tokens if word.isalpha() and not word in stop_words]
            # Stem words
            words = [porter.stem(word) for word in words]

            user.words += words
 
# time_counter = Counter(all_times)
word_counter = Counter(main_channel.words)
emoji_counter = Counter(main_channel.emojis)
print(word_counter.most_common(10))
print(emoji_counter.most_common(5))
print(main_channel.user_message_counter())
