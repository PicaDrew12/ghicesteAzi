import datetime
import json

def parse_message(line):
    parts = line.split(' - ')
    if len(parts) >= 2:
        date_str, content = parts[:2]
        try:
            datetime.datetime.strptime(date_str, '%d/%m/%y, %I:%M\u202f%p')
            sender, message = content.split(': ', 1)
            if message.strip() != '<Media omitted>' and len(message.strip()) > 50:
                return {'date': date_str.strip(), 'sender': sender.strip(), 'message': message.strip()}
        except ValueError:
            pass
    return None

def filter_messages(messages, months=5):
    current_date = datetime.datetime.now()
    filtered_messages = []
    for message in reversed(messages):
        try:
            date_str = message['date']
            date = datetime.datetime.strptime(date_str, '%d/%m/%y, %I:%M\u202f%p')
            if current_date - date < datetime.timedelta(days=30*months):
                filtered_messages.append(message)
        except ValueError:
            pass
    return filtered_messages

def main():
    with open('convo.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    messages = [parse_message(line) for line in lines if parse_message(line)]
    filtered_messages = filter_messages(messages)

    with open('messages.json', 'w', encoding='utf-8') as file:
        json.dump(filtered_messages, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
