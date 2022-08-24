import app
import os
print("hello this shouldnt appear")
port = int(os.environ.get('PORT', 33507))
app.app.run(debug=True, port=port)
