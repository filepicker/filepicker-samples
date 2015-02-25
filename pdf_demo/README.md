## PDF Viewer

Example: [http://chromakey44.appspot.com/](http://chromakey44.appspot.com/)

#### Installation

[Install Go and Google App Engine Go tools](https://cloud.google.com/appengine/docs/go/gettingstarted/introduction)

#### Configuration

1. Signup for an account on [Filepicker.io](https://www.filepicker.io) and get ApiKey.
2. Put your ApiKey to */public/javascript/picker.js*

### Running locally

```
goapp serve .
```

### Deploy to GAE

1. Edit app.yaml with your project id and version settings
2. Deploy

```
goapp deploy .
```

### Filepicker plain text presentation

1. Install mdp

```
brew install mdp
```

2. Run presentation

```
mdp demo.md
```
