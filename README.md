# discord-chat-analysis
A simple script to consume discord chat history and output interesting facts

## Prep work
### Download Discord Chat
Need to download discord chat into CSV file. Couple of different tools out there
but the best one I have found is this [one](https://github.com/Tyrrrz/DiscordChatExporter) 
by Tyrrrz

Using that CLI tool I exported the discord chat with the following command
``` bash
dotnet DiscordChatExporter.Cli.dll export -t "<discord-token>" -c <channel-id> -f Json
```

## Usage

To run the analysis simply enter
``` bash
python analysis.py <filename>
```

| Argument | Required | Details |
| - | - |
| filename | Yes | Path to exported discord chat in CSV format |
| --start-date | No | Start date for the analysis |
| --end-date | No | End date for the analysis |

## Graph Ideas
### Main channel
- Top words overall
- Top emojies
- Top responses
- Most active users
- Monthly message breakdown
- Daily (time) message breakdown

- Yearly message breakdown
- Weekend vs weekday?
- Heatmap of who talks with who
- Most edits?

### Per User
- Top words
- Top emojies
- Active times

- Weekend vs weekday?
- Top @s

## Future Work
### Main Code
Would like to move the chat export over to this repo
Make into package?

CSV/JSON output option

Get system timezone

Reaction/emoji fix. Currently relying on reaction emojis to match with message
emojis. If emoji isn't used as a reaction won't have image to download

### Graphics
Utilize avatar pictures in report

Export popular files/links

Different chart options
Overload graphing method?
