const express = require("express");
const path = require("path");
const { exec } = require("child_process");
const { translate } = require("google-translate-api-browser");

const app = express();
const port = process.env.PORT || 3000;
const languageCodes = {
    english: "en",
    french: "fr",
    spanish: "es",
    japanese: "ja",
    chinese: "zh-CN",
};

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, "public")));

// Define a route for the homepage
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/run", (req, res) => {
  const scriptPath = `"${path.join(__dirname, "../../ASL.py")}"`;
  const lang = req.query.language;
 
  exec(`python ${scriptPath} ${lang}`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing x.py: ${error}`);
        res.status(500).send("Internal Server Error");
    } else {
        const lines = stdout.trim().split("\n");
        const lastLine = lines[lines.length - 1];
        translate(lastLine, { to: languageCodes[lang] })
            .then((req,res) => {
                res.sendText(res.text); 
            })
            .catch((err) => {
                console.error(err);
            });
    }
  });
});


// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
