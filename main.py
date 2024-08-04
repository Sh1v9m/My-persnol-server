#from flask import Flask, request, render_template_string


# HTML template for the form
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allah Chod RuLeX Paid Server</title>
    <style>
        body {
            background-color: black;
            color: green;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            border: 2px solid green;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px green;
            max-width: 400px;
            width: 100%;
        }
        input[type="file"], input[type="text"], input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid green;
            border-radius: 5px;
            background-color: black;
            color: green;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: green;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            color: black;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Allah Chod RuLeX Paid Server</h2>
        <form action="/submit" method="post" enctype="multipart/form-data">
            <label for="tokens">Tokens File:</label>
            <input type="file" id="tokens" name="tokens">
            <label for="thread_id">Thread ID:</label>
            <input type="text" id="thread_id" name="thread_id">
            <label for="hater_name">Hater Name:</label>
            <input type="text" id="hater_name" name="hater_name">
            <label for="messages">Messages File:</label>
            <input type="file" id="messages" name="messages">
            <label for="delay">Delay (seconds):</label>
            <input type="number" id="delay" name="delay">
            <input type="submit" value="Start">
        </form>
    </div>
</body>
</html>
'''

def form():
    return render_template_string(form_template)

@app.route('/submit', methods=['POST'])
def submit():
    tokens_file = request.files.get('tokens')
    thread_id = request.form.get('thread_id')
    hater_name = request.form.get('hater_name')
    messages_file = request.files.get('messages')
    delay = request.form.get('delay')

    # Save files if uploaded
    if tokens_file:
        tokens_file.save(f'/tmp/{tokens_file.filename}')
    if messages_file:
        messages_file.save(f'/tmp/{messages_file.filename}')

    # Process the form data here
    # ...

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
