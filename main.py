import app
import os
port = int(os.environ.get('PORT', 33507))
app.app.run(debug=True, port=port)
