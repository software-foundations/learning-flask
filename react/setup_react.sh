# 01 -> install node and npm
sudo apt install nodejs
sudo apt install npm

# 02 -> configuration [optional]
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
source ~/.profile

# 03 -> check node and npm
node -v
npm -v

# 04 -> instalation of npx
sudo npm i -g npx

# 05 -> check npx
npx -v


###################
# -> React Creation
###################

# 01 -> creating React App
npx create-react-app react-flask-app
cd react-flask-app

# 02 -> at the end of package.json, ad the line above
"proxy": "http://localhost:5000/"


######################
# -> React Integration
#####################

# 01 -> In React's App.js file,
# add these lines to create
# react Component

import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(()=> {
    fetch('/hello').then(
      response => response.json()
    ).then(data => setInitialData(data))
    // .then(data => console.log(data))
  }, []);

  return (
    <div className="App">
      <h1>{initialData.result}</h1>
    </div>
  );

}

export default App;


# 02 -> add this line at package.json,
# just above
# 	"scripts": {
#     	"start": "react-scripts start",

"start-flask-api": "../../venv-learning-flask/bin/flask run",

# 03 -> terminal 01 Start apis
# activate the virtualenv before that
npm run start-flask-api

# 04 -> terminal 02: Start React
# activate the virtualenv before that
npm start