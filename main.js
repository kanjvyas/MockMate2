const { app, BrowserWindow } = require('electron')
const path = require('path')
const { PythonShell } = require('python-shell')

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  })

  win.loadFile('index.html')
}

app.whenReady().then(createWindow)

// Python integration
function runPythonScript(question, answer, callback) {
  let options = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: path.join(__dirname),
    args: [question, answer]
  }

  PythonShell.run('interview_analysis.py', options, (err, results) => {
    if (err) {
      console.error(err)
      return callback({ error: "Analysis failed" })
    }
    callback(JSON.parse(results[0]))
  })
}

// Expose to renderer
require('./ipcHandler')(runPythonScript)